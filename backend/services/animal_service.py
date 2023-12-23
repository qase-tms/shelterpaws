from sqlalchemy.ext.asyncio import AsyncSession as Session

from backend.dao.animal_dao import AnimalDao
from backend.models.animal import Animal
from backend.schemas.animal_schemas import AnimalCreateSchema, AnimalUpdateSchema


class AnimalService:
    def __init__(self, session: Session):
        self.session = session

    async def get_animal_by_id(self, animal_id: int) -> Animal:
        return await AnimalDao(self.session).find_one(animal_id)

    async def get_animal_list(self) -> list[Animal]:
        return await AnimalDao(self.session).find_all()

    async def create_new_animal(self, schema: AnimalCreateSchema):
        await AnimalDao(self.session).create_one(schema)

    async def update_animal(self, animal_id: int, schema: AnimalUpdateSchema):
        await AnimalDao(self.session).update_one(animal_id, schema)

    async def delete_animal_by_id(self, animal_id: int):
        await AnimalDao(self.session).delete_one(animal_id)
