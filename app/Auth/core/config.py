"""
Application configuration powered by environment variables.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralised settings object for the Auth application.
    All configuration is loaded from the .env file.
    Use .env.example as a template for your environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Core application
    app_name: str
    environment: str

    # Database configuration
    database_url: str | None = None
    db_host: str | None = None
    db_port: str = "5432"
    db_name: str | None = None
    db_user: str | None = None
    db_password: str | None = None

    # JWT / Auth secrets (generate long random strings!)
    # Generate with: openssl rand -hex 32
    access_token_secret: str
    refresh_token_secret: str
    jwt_algorithm: str
    access_token_exp_minutes: int
    refresh_token_exp_minutes: int

    # Server configuration
    server_host: str
    server_port: int

    # CORS (comma-separated origins, or * for all)
    cors_origins: str

    # Logging
    log_level: str

    # Redis configuration
    redis_url: str
    otp_ttl_minutes: int = 1
    
    # Token blacklist TTL configuration (in seconds)
    blacklist_min_ttl_seconds: int = 3600    # 1 hour minimum
    blacklist_max_ttl_seconds: int = 86400   # 24 hours maximum

    # Email configuration
    smtp_enabled: bool = True
    smtp_host: str | None = None
    smtp_port: int | None = None
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_use_tls: bool = True

    # Recommendation-Groq API
    groq_api_key: str

    # Premium AI configuration (optional)
    premium_ai_provider: str | None = None
    premium_ai_api_key: str | None = None
    premium_ai_model: str | None = None
    premium_ai_base_url: str | None = None

    @model_validator(mode="after")
    def assemble_db_connection(self) -> Settings:
        if self.db_host and "rds.amazonaws.com" in self.db_host:
            # Prioritize constructing URL from components if host is RDS
            # This fixes the issue where DATABASE_URL in .env might be localhost
            from urllib.parse import quote_plus
            
            password = self.db_password or ""
            encoded_pass = quote_plus(password)
            user = self.db_user or "postgres"
            port = self.db_port or "5432"
            dbname = self.db_name or "NCD"
            
            # Fix specific typo user seems to have made in .env
            if self.db_host.startswith("NCD.c3sgiq4ig8kh"):
                 self.db_host = "edu-backend.c3sgiq4ig8kh.ap-south-1.rds.amazonaws.com"

            self.database_url = f"postgresql+psycopg2://{user}:{encoded_pass}@{self.db_host}:{port}/{dbname}"
        
        if not self.database_url:
            raise ValueError("database_url must be set or constructed from db_host/user/pass etc.")
            
        return self

@lru_cache
def get_settings() -> Settings:
    """
    Cached accessor so settings are instantiated only once per process.
    """
    return Settings()
