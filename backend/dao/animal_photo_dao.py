from backend.dao.base_dao import BaseDao
from backend.models.animal_photo import AnimalPhoto

from sqlalchemy import delete


class AnimalPhotoDao(BaseDao):
    def __init__(self, session):
        super().__init__(session, AnimalPhoto)

    async def remove_file_by_name(self, file_name: str):
        query = delete(AnimalPhoto).where(AnimalPhoto.url == file_name)
        await self.session.execute(query)
