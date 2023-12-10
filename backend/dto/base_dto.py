from pydantic import BaseModel as PydanticBaseModel


class BaseDto(PydanticBaseModel):
    class Config:
        orm_mode = True
        extra = "forbid"


class BaseOkResponse(BaseDto):
    status: str = "ok"
