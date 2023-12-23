from backend.settings.base_settings import BaseSettings


class Settings(BaseSettings):
    SWAGGER_ENABLE: bool | None = False
