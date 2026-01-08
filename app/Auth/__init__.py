"""
Auth package for handling user authentication and authorization.

This package provides the following functionality:
- User registration and authentication
- JWT token generation and validation
- Password hashing and verification
- Protected route decorators
- Role-based access control
"""

from fastapi import APIRouter
from app.Auth.api import api_router

# Create main auth router with /auth prefix
router = APIRouter(prefix="/auth")
router.include_router(api_router)

__all__ = ["router"]
