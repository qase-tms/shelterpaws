from fastapi import Response, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession as Session
from passlib.context import CryptContext

from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError

import time

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
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        shelter = await self.__get_shelter_from_db(body.username)
        if not shelter:
            raise credentials_exception
        if not self.__verify_encoded_fields(
            body.password, hashed_field=shelter.password
        ):
            raise credentials_exception

        return self.__generate_session_token(shelter)

    async def create_shelter(self, body: CreateShelterSchema) -> Shelter:
        body.username = body.username.strip().lower()
        body.password = self.__get_password_hash(body.password)
        return await self.dao.create_shelter(body)

    async def check_is_auth_active(self, request: Request):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

        token = request.headers.get("x-auth")
        if not token:
            raise credentials_exception

        try:
            jwt.decode(token, "salt")
        except ExpiredSignatureError:
            raise credentials_exception
        except JWTError:
            raise credentials_exception

    @staticmethod
    def __verify_encoded_fields(plain_field, hashed_field):
        return pwd_context.verify(plain_field, hashed_field)

    @staticmethod
    def __get_password_hash(password):
        return pwd_context.hash(password)

    @staticmethod
    def __generate_session_token(shelter: Shelter):
        expires = time.time() + 3600
        token = jwt.encode({"username": shelter.username, "exp": expires}, "salt")
        return token

    async def __get_shelter_from_db(self, username: str):
        return await self.dao.get_shelter_from_db(username)

    async def __get_shelter_from_db_by_id(self, id: int):
        return await self.dao.get_shelter_from_db_by_id(id)
