import logging

from fastapi import FastAPI

from backend.database import PostgresAccessor


def bind_events(
        app: FastAPI, db_url: str,
        logging_enabled: bool = False
) -> None:
    @app.on_event("startup")
    async def set_engine():
        db = PostgresAccessor(db_url=db_url)
        await db.set_engine()
        app.state.db = db

    @app.on_event("shutdown")
    async def close_engine():
        await app.state.db.stop()

    if logging_enabled:
        @app.on_event("startup")
        async def set_logger():
            uvicorn_access = logging.getLogger("uvicorn.access")
            uvicorn_access.disabled = True
