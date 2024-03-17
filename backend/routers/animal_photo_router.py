from fastapi import APIRouter, UploadFile, Request
from starlette.responses import FileResponse

from backend.schemas.animal_photo_schemas import AnimalPhotoSchemaResponse
from backend.schemas.base_schema import BaseOkResponse
from backend.services.animal_photo_service import AnimalPhotoService

router = APIRouter(
    tags=["animal photo"],
    prefix="/animal_photo"
)


@router.post("/upload/{animal_id}")
async def upload_animal_photo(
        request: Request,
        file: UploadFile,
        animal_id: int
) -> AnimalPhotoSchemaResponse:
    async with request.app.state.db.get_master_session() as session:
        return await AnimalPhotoService(session).save_file(file, animal_id)


@router.get("/download/{file_name}")
async def download_animal_photo(
        request: Request,
        file_name: str
):
    async with request.app.state.db.get_master_session() as session:
        path_file = AnimalPhotoService.get_path_to_photo(file_name)
        return FileResponse(path=path_file, filename=file_name, media_type="application/octet-stream")


@router.delete("/{file_name}")
async def delete_animal_photo(
        request: Request,
        file_name: str
):
    async with request.app.state.db.get_master_session() as session:
        await AnimalPhotoService(session).remove_file(file_name)
        return BaseOkResponse()
