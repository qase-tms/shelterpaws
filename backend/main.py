import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from backend.settings import Settings
from backend.utils import bind_routes, bind_events, bind_exceptions, bind_static


def make_app(settings: Settings):
    swagger_url = None
    openapi_url = None
    redoc_url = None

    if settings.SWAGGER_ENABLE:
        swagger_url = f"{settings.URL_PREFIX}swagger"
        openapi_url = f"{settings.URL_PREFIX}openapi.json"
        redoc_url = f"{settings.URL_PREFIX}redoc"

    app = FastAPI(
        title="ShelterPaws",
        description="",
        docs_url=swagger_url,
        openapi_url=openapi_url,
        redoc_url=redoc_url
    )

    bind_routes(app)
    bind_events(app, settings.database_url)
    bind_exceptions(app)
    bind_static(app)
    add_pagination(app)

    return app


if __name__ == '__main__':
    settings = Settings()
    uvicorn.run(
        make_app(settings),
        port=settings.APP_PORT,
        host=settings.APP_HOST,
        reload=settings.APP_RELOAD
    )
