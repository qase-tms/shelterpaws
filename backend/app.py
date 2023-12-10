import uvicorn
from fastapi import FastAPI
from sqlalchemy import Engine

from backend.database import PostgresAccessor
from backend.handlers import routes
from backend.settings.base_settings import BaseSettings
from utils.bind_events import bind_events


def make_app(settings: BaseSettings):
    app = FastAPI(
        title="ShelterPaws",
        description=""
    )

    for route in routes:
        app.include_router(route)

    bind_events(app, settings.database_url)

    return app


if __name__ == '__main__':
    settings = BaseSettings()
    uvicorn.run(
        make_app(settings),
        port=settings.APP_PORT,
        host=settings.APP_HOST,
        reload=settings.APP_RELOAD
    )
