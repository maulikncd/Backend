"""
Recommendation module for website building recommendations.
"""

from fastapi import APIRouter
from app.web_builder.Recommendation.app.api import api_router

# Create main recommendation router with prefix
router = APIRouter()
router.include_router(api_router)

__all__ = ["router"]