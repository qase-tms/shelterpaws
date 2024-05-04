from operator import itemgetter

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.settings import BaseSettings



default_value = ["*"]


def prepare_cors_middleware(app: FastAPI, settings: BaseSettings):
    middleware, params = itemgetter("middleware", "params")(
        create_cors_middleware(origins=settings.cors_origins)
    )

    app.add_middleware(
        middleware,
        **params,
    )


def create_cors_middleware(
    origins: list[str] | None = None,
    methods: list[str] | None = None,
    headers: list[str] | None = None,
):
    return {
        "middleware": CORSMiddleware,
        "params": {
            "allow_origins": origins or default_value,
            "allow_credentials": True,
            "allow_methods": methods or default_value,
            "allow_headers": headers or default_value,
        },
    }
