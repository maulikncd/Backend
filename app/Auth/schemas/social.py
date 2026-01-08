"""
Pydantic schemas for social authentication endpoints.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class SocialLoginRequest(BaseModel):
    username: str = Field(..., description="Username from social provider")
    email: EmailStr
    login_method: str = Field(..., description="Social provider (google, facebook, apple, etc.)")
    social_id: str = Field(..., description="Social provider user ID")
    picture: Optional[str] = Field(default=None, description="Profile picture URL")
    device_id: Optional[str] = Field(default=None, max_length=255)
    device_name: Optional[str] = Field(default=None, max_length=255)
    location: Optional[str] = Field(default=None, max_length=255)


class SocialLoginResponseData(BaseModel):
    user_id: int
    email: EmailStr
    username: str
    access_token: str
    refresh_token: str


class SocialLoginResponse(BaseModel):
    status: bool = True
    message: str = Field(default="Login successful")
    data: SocialLoginResponseData


# Backward compatibility aliases
GoogleLoginRequest = SocialLoginRequest
GoogleLoginResponse = SocialLoginResponse
GoogleLoginResponseData = SocialLoginResponseData
