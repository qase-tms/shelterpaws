from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    DB_TYPE: str | None = None
    DB_ENGINE: str | None = None
    PATH_TO_DATABASE: str | None = None
    DB_HOST: str | None = None
    DB_PORT: str | None = None
    DB_USER: str | None = None
    DB_PASSWORD: str | None = None
    DB_NAME: str | None = None

    APP_PORT: int | None = 8080
    APP_HOST: str | None = "localhost"
    APP_RELOAD: bool = False

    @property
    def database_url(self) -> str:
        return f"{self.DB_TYPE}+{self.DB_ENGINE}:///{self.PATH_TO_DATABASE}"
