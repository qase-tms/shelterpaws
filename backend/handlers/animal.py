from fastapi import APIRouter, Request

from backend.dao.animal_dao import AnimalDao
from backend.dto.animal_dto import AnimalResponseDto, AnimalCreateDto, AnimalUpdateDto
from backend.dto.base_dto import BaseOkResponse

router = APIRouter(
    tags=["animals"],
    prefix="/animals"
)


@router.get("/")
async def get_animals(
        request: Request
) -> list[AnimalResponseDto]:
    async with request.app.state.db.get_master_session() as session:
        animal_dao = AnimalDao(session)
        return await animal_dao.find_all()


@router.get("/{animal_id}")
async def get_animal_by_id(
        request: Request,
        animal_id: int
) -> AnimalResponseDto:
    async with request.app.state.db.get_master_session() as session:
        animal_dao = AnimalDao(session)
        return await animal_dao.find_one(animal_id)


@router.post("/")
async def create_animal(
        request: Request,
        body: AnimalCreateDto
) -> BaseOkResponse:
    async with request.app.state.db.get_master_session() as session:
        animal_dao = AnimalDao(session)
        await animal_dao.create_one(body)
        return BaseOkResponse()


@router.put("/{animal_id}")
async def update_animal(
        request: Request,
        animal_id: int,
        body: AnimalUpdateDto
) -> BaseOkResponse:
    async with request.app.state.db.get_master_session() as session:
        animal_dao = AnimalDao(session)
        await animal_dao.update_one(animal_id, body)
        return BaseOkResponse()


@router.delete("/{animal_id}")
async def update_animal(
        request: Request,
        animal_id: int
) -> BaseOkResponse:
    async with request.app.state.db.get_master_session() as session:
        animal_dao = AnimalDao(session)
        await animal_dao.delete_one(animal_id)
        return BaseOkResponse()
