from backend.schemas.base_schema import BaseSchema


class AnimalBaseSchema(BaseSchema):
    name_ru: str
    name_en: str


class AnimalResponseSchema(AnimalBaseSchema):
    id: int


class AnimalCreateSchema(AnimalBaseSchema):
    ...


class AnimalUpdateSchema(AnimalBaseSchema):
    ...
