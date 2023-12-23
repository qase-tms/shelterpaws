from backend.schemas.base_schema import BaseSchema


class AnimalPhotoSchemaResponse(BaseSchema):
    id: int
    full_url: str


class AnimalPhotoSchemaCreate(BaseSchema):
    animal_id: int
    url: str
