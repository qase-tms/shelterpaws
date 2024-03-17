import os
import uuid
from pathlib import Path

from fastapi import UploadFile, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession as Session

from backend.dao.animal_photo_dao import AnimalPhotoDao
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

        path_file: Path = AnimalPhotoService.get_path_to_photo(file_name)

        if not path_file.exists():
            path_file.write_bytes(await file.read())

            file_model = AnimalPhotoSchemaCreate(
                animal_id=animal_id,
                url=file_name
            )

            return await AnimalPhotoDao(self.session).create_one(file_model)
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"file {file_name} already exist"
            )

    @staticmethod
    def get_path_to_photo(file_name: str):
        return Path(f"{AnimalPhotoService.__path_to_photos}/{file_name}")

    async def remove_file(self, file_name: str):
        await AnimalPhotoDao(self.session).remove_file_by_name(file_name)
        full_path = AnimalPhotoService.get_path_to_photo(file_name)
        if os.path.exists(full_path):
            os.remove(full_path)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"file {file_name} not found"
            )
