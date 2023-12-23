from pydantic import BaseModel as PydanticBaseModel


class BaseSchema(PydanticBaseModel):
    class Config:
        from_attributes = True
        extra = "forbid"


class BaseOkResponse(BaseSchema):
    status: str = "ok"
