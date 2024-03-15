import enum
from fastapi import HTTPException
from starlette import status

from sqlalchemy.exc import IntegrityError

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseDao:
    def __init__(
            self,
            session: AsyncSession,
            model
    ):
        self.session = session
        self.model = model

    async def find_all(self):
        query = select(self.model)
        return (await self.session.execute(query)).unique().scalars().all()

    async def find_one(self, model_id):
        query = select(self.model)
        query = query.where(self.model.id == model_id)

        model = (await self.session.execute(query)).scalars().first()

        if not model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Model with {model_id} is not found", )

        return model

    async def create_one(self, schema):
        try:
            model = self.model(**schema.dict())
            self.session.add(model)
            await self.session.flush()
            await self.session.refresh(model)
            return model
        except IntegrityError as err:
            print(err.detail)

    async def update_one(self, model_id, schema):
        model = await self.find_one(model_id)
        self.__update_model_fields(model, schema)
        try:
            await self.session.flush()
        except IntegrityError as err:
            print(err.detail)

        return model

    async def delete_one(self, model_id):
        model = await self.find_one(model_id)
        await self.session.delete(model)
        try:
            await self.session.flush()
        except IntegrityError as err:
            await self.session.rollback()

    @staticmethod
    def __update_model_fields(model, schema):
        for key, value in schema.dict().items():
            if isinstance(value, enum.Enum):
                setattr(model, key, value.value)
            else:
                setattr(model, key, value)
