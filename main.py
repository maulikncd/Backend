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
    # CORS Configuration
    origins = [
        "http://localhost:5173",  # Vite default
        "http://localhost:3000",  # React default
        "http://localhost:5174",  # Vite alternative
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
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
        try:
            init_db()
            print("✅ Database tables initialized successfully.")
        except Exception as e:
            print(f"⚠️  Database connection failed: {e}")
            print("❗ IF USING AWS RDS: Please check your Security Group 'Inbound rules'.")
            print("   Ensure port 5432 is open for your IP address.")
            print("   The server will start, but database operations will fail until connectivity is fixed.")

    return app


app = create_app()
