from backend.dao.base_dao import BaseDao
from backend.models.animal_photo import AnimalPhoto
from sqlalchemy.ext.asyncio import AsyncSession as Session


class AnimalPhotoDao(BaseDao):
    def __init__(self, session):
        super().__init__(session, AnimalPhoto)
