"""
Pydantic schemas for authentication endpoints.
"""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class SignupRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=100, description="Username must be at least 3 characters long")
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72, description="Password must be at least 6 characters long")
    confirm_password: str = Field(..., min_length=6, max_length=72, description="Password must be at least 6 characters long")
    login_method: Literal["manual"] = "manual"
    device_id: Optional[str] = Field(default=None, max_length=255)
    device_name: Optional[str] = Field(default=None, max_length=255)
    location: Optional[str] = Field(default=None, max_length=255)

    @field_validator("username")
    @classmethod
    def username_rules(cls, value: str) -> str:
        if len(value.strip()) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if value.isdigit():
            raise ValueError("Username cannot be only digits")
        return value

    @field_validator("password", "confirm_password")
    @classmethod
    def password_length(cls, value: str) -> str:
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long")
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password cannot exceed 72 bytes due to bcrypt limits")
        return value

    @field_validator("login_method")
    @classmethod
    def ensure_manual_login(cls, value: str) -> str:
        if value != "manual":
            raise ValueError("Only manual signup is supported")
        return value

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, value: str, info) -> str:
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("Passwords do not match")
        return value


class SignupResponseData(BaseModel):
    user_id: int
    email: EmailStr
    access_token: str
    refresh_token: str


class SignupResponse(BaseModel):
    status: Literal[True] = True
    message: str = Field(default="Account created successfully")
    data: SignupResponseData


class OTPRequest(BaseModel):
    email: EmailStr


class OTPResponse(BaseModel):
    status: Literal[True] = True
    message: str = Field(default="OTP sent successfully")


class OTPVerifyOnlyResponse(BaseModel):
    status: Literal[True] = True
    message: str = Field(default="OTP verified successfully")


class OTPVerifyRequest(BaseModel):
    email: EmailStr
    otp: str = Field(..., min_length=6, max_length=6, description="6-digit OTP")


class OTPVerifyResponseData(BaseModel):
    user_id: int
    email: EmailStr
    username: str
    access_token: str
    refresh_token: str


class OTPVerifyResponse(BaseModel):
    status: Literal[True] = True
    message: str = Field(default="Email verified successfully")
    data: OTPVerifyResponseData


# Schema aliases for backward compatibility
SignupSchema = SignupRequest
VerifyOTPSchema = OTPVerifyRequest
