from backend.schemas.base_schema import BaseSchema


class AnimalBaseSchema(BaseSchema):
    name_ru: str
    name_en: str


class AnimalSimpleResponseSchema(AnimalBaseSchema):
    id: int
    last_photo: str | None


class AnimalFullResponseSchema(AnimalSimpleResponseSchema):
    photo_urls: list[str] = []


class AnimalCreateSchema(AnimalBaseSchema):
    ...


class AnimalUpdateSchema(AnimalBaseSchema):
    ...
