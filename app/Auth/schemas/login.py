"""
Pydantic schemas for login endpoints.
"""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    login_method: Literal["manual"] = "manual"
    device_id: Optional[str] = Field(default=None, max_length=255)
    device_name: Optional[str] = Field(default=None, max_length=255)
    location: Optional[str] = Field(default=None, max_length=255)

    @field_validator("login_method")
    @classmethod
    def ensure_manual_login(cls, value: str) -> str:
        if value != "manual":
            raise ValueError("Only manual login is supported")
        return value


class LoginResponseData(BaseModel):
    user_id: int
    email: EmailStr
    username: str
    access_token: str
    refresh_token: str


class LoginResponse(BaseModel):
    status: Literal[True] = True
    message: str = Field(default="Login successful")
    data: LoginResponseData
