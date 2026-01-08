"""
Web_generator module for website building and code generation.
"""

from fastapi import APIRouter
from app.web_builder.Web_generator.app.api import api_router

# Create main web_generator router with prefix
router = APIRouter()
router.include_router(api_router)

__all__ = ["router"]