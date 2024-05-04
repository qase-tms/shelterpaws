from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    DB_HOST: str | None
    DB_PORT: str | None
    DB_USER: str | None
    DB_PASSWORD: str | None
    DB_NAME: str | None

    APP_HOST: str | None = "0.0.0.0"
    APP_PORT: int | None = 8080

    HTTP_PROTOCOL: str | None = "https"

    URL_PREFIX: str | None = "/api/v1/shelterpaws/"

    LOGGING_MIDDLEWARE_ENABLED: bool = True
    SWAGGER_ENABLE: bool | None = True

    APP_RELOAD: bool = False

    PATH_TO_PHOTOS: str | None = "./animal_photos"
    URL_PHOTO_DOWNLOAD: str | None

    CORS: list[str] | None

    @property
    def cors_origins(self):
        return self.CORS

    @property
    def db_settings(self):
        return {
            "database": self.DB_NAME,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD,
            "host": self.DB_HOST,
            "port": self.DB_PORT,
            "logging": self.LOGGING_MIDDLEWARE_ENABLED,
            "app_host": self.APP_HOST,
            "app_port": self.APP_PORT,
        }

    @property
    def database_url(self):
        return (
            "postgresql+asyncpg://"
            "{user}:{password}@{host}:{port}"
            "/{database}?ssl=require".format(**self.db_settings)
        )
