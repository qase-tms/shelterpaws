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


class AnimalResponseSchema(AnimalBaseSchema):
    id: int


class AnimalCreateSchema(AnimalBaseSchema):
    type: str
    sex: str
    age: str
    size: str


class AnimalUpdateSchema(AnimalBaseSchema):
    ...
