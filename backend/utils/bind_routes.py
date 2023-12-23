from backend.routers import routes
from fastapi import FastAPI


def bind_routes(app: FastAPI):
    for route in routes:
        app.include_router(route)
