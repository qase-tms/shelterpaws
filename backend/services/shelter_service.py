from fastapi import Response, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession as Session
from passlib.context import CryptContext

from os import environ
import time
import json

from backend.models.shelter import Shelter
from backend.schemas.shelter_schemas import (
    CreateShelterSchema,
    BaseShelterSchema,
)
from backend.dao.shelter_dao import ShelterDao


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ShelterService:
    def __init__(self, session: Session):
        self.session = session
        self.dao = ShelterDao(session)

    async def authenticate_shelter(self, body: BaseShelterSchema, response: Response):
        shelter = await self.__get_shelter_from_db(body.username)
        if not shelter:
            return False
        if not self.__verify_encoded_fields(
            body.password, hashed_field=shelter.password
        ):
            return False
        self.__prepare_cookie(shelter, response)
        return shelter

    async def create_shelter(self, body: CreateShelterSchema) -> Shelter:
        body.username = body.username.strip().lower()
        body.password = self.__get_password_hash(body.password)
        return await self.dao.create_shelter(body)

    async def check_is_auth_active(self, request: Request, response: Response):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

        shelter_id = request.cookies.get("shelter-id")
        auth_cookie = request.cookies.get("x-auth")

        if not shelter_id or not auth_cookie:
            response.delete_cookie("shelter-id")
            response.delete_cookie("x-auth")
            raise credentials_exception

        shelter = await self.__get_shelter_from_db_by_id(int(shelter_id))
        secret_field = self.__prepare_secret_field(shelter)

        if not self.__verify_encoded_fields(secret_field, auth_cookie):
            response.delete_cookie("shelter-id")
            response.delete_cookie("x-auth")
            raise credentials_exception

    def __verify_encoded_fields(self, plain_field, hashed_field):
        return pwd_context.verify(plain_field, hashed_field)

    def __get_password_hash(self, password):
        return pwd_context.hash(password)

    async def __get_shelter_from_db(self, username: str):
        return await self.dao.get_shelter_from_db(username)

    async def __get_shelter_from_db_by_id(self, id: int):
        return await self.dao.get_shelter_from_db_by_id(id)

    def __prepare_secret_field(self, shelter):
        field_to_select = environ.get("HASH_FIELD", "username")
        selected_value = getattr(shelter, field_to_select, field_to_select)
        secret = json.dumps(
            {
                "id": shelter.id,
                "secret": selected_value,
            }
        )

        return secret

    def __prepare_cookie(self, shelter, response: Response):
        secret_field = self.__prepare_secret_field(shelter)
        auth_cookie = pwd_context.hash(secret_field)
        response.set_cookie(key="x-auth", httponly=True, value=auth_cookie,  samesite='none', secure=True)
        response.set_cookie(key="shelter-id", httponly=True, value=shelter.id, samesite='none', secure=True)
