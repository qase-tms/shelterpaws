from backend.schemas.base_schema import BaseSchema


class AnimalIndexSchema(BaseSchema):
    link: str = '#'
    type: str
    img_src: str
    name: str
    sex: str
    age: str
    size: str

class AnimalBaseSchema(BaseSchema):
    name_ru: str
    name_en: str


class AnimalSimpleResponseSchema(AnimalBaseSchema):
    id: int
    last_photo: str | None


class AnimalFullResponseSchema(AnimalSimpleResponseSchema):
    photo_urls: list[str] = []


class AnimalCreateSchema(AnimalBaseSchema):
    type: str
    sex: str
    age: str
    size: str
    shelter_id: int


class AnimalUpdateSchema(AnimalBaseSchema):
    ...
