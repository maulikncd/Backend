from fastapi import APIRouter
from .v1.recommendation import router as recommendation_router

api_router = APIRouter()
api_router.include_router(recommendation_router, prefix="/recommendation", tags=["Recommendation"])