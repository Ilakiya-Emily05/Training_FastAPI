from fastapi import FastAPI

# Routers
from app.controllers.user_controller import router as user_router
from app.controllers.product_controller import router as product_router
from app.controllers.application_controller import router as application_router
from app.controllers.repayment_controller import router as repayment_router

# Middleware
from app.middleware.cors import setup_cors
from app.middleware.logging_middleware import logging_middleware

# Exceptions
from app.exceptions.custom_exceptions import (
    NotFoundException,
    BadRequestException,
    UnauthorizedException,
)
from app.exceptions.exception_handlers import (
    not_found_exception_handler,
    bad_request_exception_handler,
    unauthorized_exception_handler,
)

app = FastAPI(
    title="Banking LMS",
    version="1.0.0",
)

setup_cors(app)
app.middleware("http")(logging_middleware)

app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)


app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(product_router, prefix="/products", tags=["Loan Products"])
app.include_router(application_router, prefix="/applications", tags=["Loan Applications"])
app.include_router(repayment_router, prefix="/repayments", tags=["Repayments"])


@app.on_event("startup")
async def startup_event():
    print(" Banking LMS API starting up")


@app.on_event("shutdown")
async def shutdown_event():
    print("Banking LMS API shutting down")