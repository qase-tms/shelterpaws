import logging

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


def bind_exceptions(app: FastAPI):
    @app.exception_handler(Exception)
    async def unhandled_error(
            request: Request,
            exc: Exception
    ):
        logger.exception(exc)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Something went wrong"},
        )
