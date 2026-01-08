"""
API router aggregation for the Auth module.
"""

from __future__ import annotations
from fastapi import APIRouter
from app.Auth.api.v1.auth import router as auth_router
from app.Auth.api.v1.other import router as other_router
from app.Auth.api.v1.social import router as social_router
from app.Auth.api.v1.forgot_password import router as forgot_password_router
from app.Auth.api.v1.change_password import router as change_password_router
from app.Auth.api.v1.projects import router as projects_router

# Create main API router with /auth prefix
api_router = APIRouter()

# Include all version 1 API routes directly under /auth
api_router.include_router(auth_router)
api_router.include_router(other_router)
api_router.include_router(social_router)
api_router.include_router(forgot_password_router)
api_router.include_router(change_password_router)
api_router.include_router(projects_router)

__all__ = ["api_router"]
