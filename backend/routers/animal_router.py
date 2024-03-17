from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from backend.schemas.animal_schemas import (
    AnimalCreateSchema,
    AnimalUpdateSchema,
    AnimalSimpleResponseSchema,
    AnimalFullResponseSchema
)
from backend.schemas.base_schema import BaseOkResponse
from backend.services.animal_service import AnimalService
from backend.services.animal_template_service import AnimalTemplateService

router = APIRouter(
    tags=["animals"],
    prefix="/animals"
)


@router.get('/index')
async def get_index_template(
        request: Request,
) -> HTMLResponse:
    async with request.app.state.db.get_master_session() as session:
        return await AnimalTemplateService(request, session).get_index_template()


@router.get("/")
async def get_animals(
        request: Request
) -> list[AnimalSimpleResponseSchema]:
    async with request.app.state.db.get_master_session() as session:
        return await AnimalService(session).get_animal_list()


@router.get("/{animal_id}")
async def get_animal_by_id(
        request: Request,
        animal_id: int
) -> AnimalFullResponseSchema:
    async with request.app.state.db.get_master_session() as session:
        return await AnimalService(session).get_animal_by_id(animal_id)


@router.post("/")
async def create_animal(
        request: Request,
        schema: AnimalCreateSchema
) -> BaseOkResponse:
    async with request.app.state.db.get_master_session() as session:
        await AnimalService(session).create_new_animal(schema)
        return BaseOkResponse()


@router.put("/{animal_id}")
async def update_animal(
        request: Request,
        animal_id: int,
        schema: AnimalUpdateSchema
) -> BaseOkResponse:
    async with request.app.state.db.get_master_session() as session:
        await AnimalService(session).update_animal(animal_id, schema)
        return BaseOkResponse()


@router.delete("/{animal_id}")
async def update_animal(
        request: Request,
        animal_id: int
) -> BaseOkResponse:
    async with request.app.state.db.get_master_session() as session:
        await AnimalService(session).delete_animal_by_id(animal_id)
        return BaseOkResponse()
