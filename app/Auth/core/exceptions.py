"""
Custom exception hierarchy for the Auth service.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import status


class ApplicationError(Exception):
    """
    Base class for all domain-level errors we want to surface to clients.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: str = "APPLICATION_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}


class ResourceConflictError(ApplicationError):
    """
    Raised when attempting to create a resource that conflicts with an existing one.
    """

    def __init__(
        self,
        message: str = "Resource already exists",
        *,
        error_code: str = "RESOURCE_CONFLICT",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            message,
            status_code=status.HTTP_409_CONFLICT,
            error_code=error_code,
            details=details,
        )


class ValidationServiceError(ApplicationError):
    """
    Raised when a domain validation fails but pydantic already accepted the payload.
    """

    def __init__(
        self,
        message: str,
        *,
        error_code: str = "DOMAIN_VALIDATION_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            message,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_code=error_code,
            details=details,
        )
