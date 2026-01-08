"""
Application entrypoint for the Website Builder backend.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.Auth import router as auth_router
from app.Auth.api.v1.projects import router as projects_router
from app.web_builder.Recommendation.app import router as recommendation_router
from app.web_builder.Web_generator.app import router as web_generator_router
from app.Auth.core.config import get_settings
from app.Auth.core.error_handlers import register_exception_handlers
from app.Auth.db.session import init_db


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="1.0.0")

    # CORS Configuration - Allow all origins for development
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_exception_handlers(app)
    # Include auth routes
    app.include_router(auth_router)
    app.include_router(recommendation_router)
    app.include_router(web_generator_router, prefix="/web-generator")
    app.include_router(web_generator_router) # Backward compatibility for root level routes
    app.include_router(projects_router) # Expose project routes at root level



    @app.on_event("startup")
    def _startup() -> None:
        init_db()

    return app


app = create_app()
