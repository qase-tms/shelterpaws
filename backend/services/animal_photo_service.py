import os
import uuid
from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession as Session

from backend.dao.animal_photo_dao import AnimalPhotoDao
from backend.models.animal_photo import AnimalPhoto
from backend.schemas.animal_photo_schemas import AnimalPhotoSchemaCreate
from backend.settings import Settings


class AnimalPhotoService:
    __path_to_photos = Settings().PATH_TO_PHOTOS

    def __init__(
            self,
            session: Session
    ):
        self.session = session

    async def save_file(self, file: UploadFile, animal_id: int):
        file_ext = os.path.splitext(file.filename)[1]
        file_name = f"{str(uuid.uuid4())}{file_ext}"

        path_file = Path(f"{AnimalPhotoService.__path_to_photos}/{file_name}")
        path_file.write_bytes(await file.read())

        file_model = AnimalPhotoSchemaCreate(
            animal_id=animal_id,
            url=file_name
        )

        return await AnimalPhotoDao(self.session).create_one(file_model)

    @staticmethod
    async def get_path_to_photo(file_name: str):
        return Path(f"{AnimalPhotoService.__path_to_photos}/{file_name}")

    async def remove_file(self, file_name: str):
        await AnimalPhotoDao(self.session).remove_file_by_name(file_name)
        full_path = await AnimalPhotoService.get_path_to_photo(file_name)
        if os.path.exists(full_path):
            os.remove(full_path)
