from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    NotFoundException,
    BadRequestException,
    UnauthorizedException,
)


async def not_found_exception_handler(
    request: Request,
    exc: NotFoundException
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": exc.message},
    )


async def bad_request_exception_handler(
    request: Request,
    exc: BadRequestException
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.message},
    )


async def unauthorized_exception_handler(
    request: Request,
    exc: UnauthorizedException
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": exc.message},
    )