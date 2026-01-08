"""
Token related schemas.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class TokenRefreshRequest(BaseModel):
    """Schema for token refresh request."""
    refresh_token: str = Field(..., description="The refresh token")


class LogoutRequest(BaseModel):
    """Schema for logout request."""
    refresh_token: str = Field(..., description="The refresh token to invalidate")


class LogoutResponseData(BaseModel):
    """Schema for logout response data."""
    message: str = Field(..., description="Logout message")
    logged_out_at: str = Field(..., description="ISO timestamp of logout")
    login_id: int = Field(..., description="Login record ID")


class LogoutResponse(BaseModel):
    """Schema for logout response."""
    status: str = Field(default="success", description="Response status")
    message: str = Field(..., description="Response message")
    data: LogoutResponseData = Field(..., description="Logout data")


class TokenResponseData(BaseModel):
    """Schema for token response data."""
    access_token: str = Field(..., description="The access token")
    refresh_token: str = Field(..., description="The refresh token")


class TokenResponse(BaseModel):
    """Schema for token response."""
    status: str = Field(default="success", description="Response status")
    message: str = Field(..., description="Response message")
    data: TokenResponseData = Field(..., description="Token data")
