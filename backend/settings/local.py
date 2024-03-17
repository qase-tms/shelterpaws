from backend.settings.base_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str | None = "localhost"
    DB_PORT: str | None = "5432"
    DB_USER: str | None = "postgres"
    DB_PASSWORD: str | None = "postgres"
    DB_NAME: str | None = "postgres"

    APP_HOST: str | None = "0.0.0.0"
    APP_PORT: int | None = 8080

    LOGGING_MIDDLEWARE_ENABLED: bool = False
    SWAGGER_ENABLE: bool = True

    URL_PHOTO_DOWNLOAD: str = "http://localhost:8080/animal_photo/download"

    @property
    def database_url(self):
        return (
            "postgresql+asyncpg://"
            "{user}:{password}@{host}:{port}"
            "/{database}?".format(**self.db_settings)
        )
