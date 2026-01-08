"""
FastAPI exception handlers for the Auth service.
"""

from __future__ import annotations

import logging
from typing import List

from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .exceptions import ApplicationError
from .response import error_response

logger = logging.getLogger(__name__)


def _format_validation_message(errors: List[dict]) -> str:
    """Format Pydantic validation errors into user-friendly messages."""
    formatted = []
    for error in errors:
        message = error.get("msg", "Invalid input")
        loc = error.get("loc", [])
        field = loc[-1] if loc else ""  # Get the actual field name (last element in loc)
        
        # Strip Pydantic prefixes like "Value error, " or "Assertion error, "
        if ", " in message:
            message = message.split(", ", 1)[-1]
        
        # Replace generic Pydantic messages with user-friendly ones based on field
        if field == "username":
            if message == "String should have at least 3 characters":
                message = "Username must be at least 3 characters long"
        elif field == "password" or field == "confirm_password":
            if message == "String should have at least 6 characters":
                message = "Password must be at least 6 characters long"
        elif field == "otp":
            if message == "String should have at least 6 characters":
                message = "OTP must be exactly 6 digits long"
            elif message == "String should have at most 6 characters":
                message = "OTP must be exactly 6 digits long"
        elif message == "Input should be 'manual'":
            message = "Only manual login is supported"
        
        formatted.append(message)
    return formatted[0] if formatted else "Validation error"


def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """Handle FastAPI HTTPExceptions."""
    logger.warning(f"HTTP exception: {exc.detail}")
    
    # Check if error code is in headers
    error_code = "HTTP_ERROR"
    if hasattr(exc, 'headers') and exc.headers and 'X-Error-Code' in exc.headers:
        error_code = exc.headers['X-Error-Code']
    
    payload = error_response(exc.detail, error_code)
    return JSONResponse(status_code=exc.status_code, content=payload)


def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    """Handle Pydantic validation errors."""
    errors_details = exc.errors()
    logger.warning(f"Validation error details: {errors_details}")
    message = _format_validation_message(errors_details)
    logger.warning(f"Validation error formatted: {message}")
    payload = error_response(message, error_code="VALIDATION_ERROR")
    return JSONResponse(status_code=422, content=payload)


def application_exception_handler(_: Request, exc: ApplicationError) -> JSONResponse:
    """Handle custom application exceptions."""
    # Log details internally but don't expose them to users
    if exc.details:
        logger.debug(f"Application error: {exc.message} | Details: {exc.details}")
    else:
        logger.debug(f"Application error: {exc.message}")
    
    payload = error_response(exc.message, error_code=exc.error_code)
    return JSONResponse(status_code=exc.status_code, content=payload)


def general_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {type(exc).__name__}: {exc}", exc_info=True)
    payload = error_response("Internal server error", error_code="INTERNAL_ERROR")
    return JSONResponse(status_code=500, content=payload)


def register_exception_handlers(app) -> None:
    """Register all exception handlers with the FastAPI app."""
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(ApplicationError, application_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
