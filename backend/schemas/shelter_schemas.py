from backend.schemas.base_schema import BaseSchema

from pydantic import Field

class BaseShelterSchema(BaseSchema):
    username: str = Field(max_length=100)
    password: str = Field(max_length=100)

class CreateShelterSchema(BaseShelterSchema):
    slug: str = Field(max_length=50)
