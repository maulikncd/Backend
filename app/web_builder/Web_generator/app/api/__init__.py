from fastapi import APIRouter
from .v1.project import router as project_router
from .v1.conversation import router as conversation_router

api_router = APIRouter()
api_router.include_router(project_router, prefix="/project", tags=["Project"])
api_router.include_router(conversation_router, tags=["Conversation & Chat"])