from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession as Session

from backend.models.shelter import Shelter
from backend.schemas.shelter_schemas import CreateShelterSchema
from backend.dao.base_dao import BaseDao


class ShelterDao(BaseDao):
    def __init__(self, session: Session):
        super().__init__(session, Shelter)

    async def create_shelter(self, body: CreateShelterSchema) -> Shelter:
        shelter = Shelter(
            username=body.username, password=body.password, slug=body.slug
        )

        self.session.add(shelter)
        await self.session.flush()

        return shelter

    async def get_shelter_from_db(self, username: str):
        query = select(Shelter).where(Shelter.username == username.lower())
        return await self.session.scalar(query)

    async def get_shelter_from_db_by_id(self, id: int):
        query = select(Shelter).where(Shelter.id == id)
        return await self.session.scalar(query)
