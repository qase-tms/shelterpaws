from fastapi import APIRouter, Request, Response

from backend.schemas.shelter_schemas import (
    CreateShelterSchema,
    BaseShelterSchema,
)
from backend.schemas.base_schema import BaseOkResponse
from services.shelter_service import ShelterService


router = APIRouter(tags=["shelter"], prefix="/shelter")


@router.get("/check")
async def check_auth(request: Request, response: Response):
    async with request.app.state.db.get_master_session() as session:
        await ShelterService(session).check_is_auth_active(request, response)
        return BaseOkResponse()


@router.post("/auth")
async def auth(request: Request, body: BaseShelterSchema, response: Response):
    async with request.app.state.db.get_master_session() as session:
        await ShelterService(session).authenticate_shelter(body, response)
        return BaseOkResponse()


@router.post("/")
async def create_shelter(
    request: Request, schema: CreateShelterSchema
) -> BaseOkResponse:
    print(request.cookies)
    async with request.app.state.db.get_master_session() as session:
        await ShelterService(session).create_shelter(schema)
        return BaseOkResponse()
