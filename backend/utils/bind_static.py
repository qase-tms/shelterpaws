from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

def bind_static(app: FastAPI):
    app.mount(
        "/static",
        StaticFiles(directory="./backend/static"),
        name="static",
    )
