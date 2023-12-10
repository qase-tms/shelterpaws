from backend.dto.base_dto import BaseDto


class AnimalBaseDto(BaseDto):
    name_ru: str
    name_en: str


class AnimalResponseDto(AnimalBaseDto):
    id: int


class AnimalCreateDto(AnimalBaseDto):
    ...


class AnimalUpdateDto(AnimalBaseDto):
    ...
