"""
Forgot Password API routes for password reset functionality.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy.orm import Session

from app.Auth.core.response import success_response, error_response
from app.Auth.core.security import hash_password
from app.Auth.db.session import get_db
from app.Auth.models.user import User
from app.Auth.utils.otp_service import OTPService

router = APIRouter(tags=["Forgot Password"])


# Schemas
class SendOTPRequest(BaseModel):
    """Schema for sending OTP request."""
    email: EmailStr = Field(..., description="User's email address")


class VerifyOTPRequest(BaseModel):
    """Schema for verifying OTP request."""
    email: EmailStr = Field(..., description="User's email address")
    otp: str = Field(..., min_length=6, max_length=6, description="6-digit OTP")


class ResetPasswordRequest(BaseModel):
    """Schema for resetting password request."""
    email: EmailStr = Field(..., description="User's email address")
    new_password: str = Field(..., min_length=6, description="New password (min 6 characters)")
    confirm_password: str = Field(..., description="Confirm new password")


@router.post(
    "/forgot-password/send-otp",
    status_code=status.HTTP_200_OK,
)
async def send_forgot_password_otp(
    payload: SendOTPRequest,
    db: Session = Depends(get_db),
):
    """
    Send OTP for password reset.
    
    Rules:
    - If forgot_pwd_otp:{email} exists → return "OTP already sent, please wait"
    - If forgot_pwd_verified:{email} exists → return "OTP already verified, reset password"
    - Generate 6-digit OTP with 1-minute TTL
    - Send OTP via SMTP
    """
    redis_client = await OTPService.get_redis_client()
    from app.Auth.core.config import get_settings
    settings = get_settings()
    
    # Check if OTP already sent
    otp_key = f"forgot_pwd_otp:{payload.email}"
    if await redis_client.exists(otp_key):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="OTP already sent, please wait",
            headers={"X-Error-Code": "OTP_ALREADY_SENT"}
        )
    
    # Check if already verified
    verified_key = f"forgot_pwd_verified:{payload.email}"
    if await redis_client.exists(verified_key):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP already verified, reset password",
            headers={"X-Error-Code": "OTP_ALREADY_VERIFIED"}
        )
    
    # Check if user exists
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not found",
            headers={"X-Error-Code": "EMAIL_NOT_FOUND"}
        )
    
    # Generate and store OTP
    otp = OTPService.generate_otp(6)
    await redis_client.setex(otp_key, 60, otp)  # 1 minute TTL
    
    # Send OTP via email
    email_sent = await OTPService.send_forgot_password_otp(payload.email, otp)
    
    if not email_sent:
        await redis_client.delete(otp_key)  # Clean up if email fails
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP email",
            headers={"X-Error-Code": "EMAIL_SEND_FAILED"}
        )
    
    return {
        "status": True,
        "message": "OTP sent to your email"
    }


@router.post(
    "/forgot-password/verify-otp",
    status_code=status.HTTP_200_OK,
)
async def verify_forgot_password_otp(
    payload: VerifyOTPRequest,
):
    """
    Verify OTP for password reset.
    
    Rules:
    - Validate OTP from Redis
    - If invalid or expired → error
    - If valid: delete forgot_pwd_otp:{email} and create forgot_pwd_verified:{email} with 5-minute TTL
    """
    redis_client = await OTPService.get_redis_client()
    
    otp_key = f"forgot_pwd_otp:{payload.email}"
    stored_otp = await redis_client.get(otp_key)
    
    if stored_otp is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP expired or not found",
            headers={"X-Error-Code": "OTP_EXPIRED"}
        )
    
    if stored_otp != payload.otp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid OTP",
            headers={"X-Error-Code": "INVALID_OTP"}
        )
    
    # Delete the OTP after successful verification
    await redis_client.delete(otp_key)
    
    # Create verification key with 5-minute TTL
    verified_key = f"forgot_pwd_verified:{payload.email}"
    await redis_client.setex(verified_key, 300, "verified")  # 5 minutes
    
    return {
        "status": True,
        "message": "OTP verified successfully"
    }


@router.post(
    "/forgot-password/reset-password",
    status_code=status.HTTP_200_OK,
)
async def reset_password(
    payload: ResetPasswordRequest,
    db: Session = Depends(get_db),
):
    """
    Reset password after OTP verification.
    
    Rules:
    - Allow reset only if forgot_pwd_verified:{email} exists
    - Hash and update password in DB
    - Delete verification key after success
    """
    # Validate passwords match
    if payload.new_password != payload.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
            headers={"X-Error-Code": "PASSWORDS_MISMATCH"}
        )
    
    redis_client = await OTPService.get_redis_client()
    
    # Check if verified
    verified_key = f"forgot_pwd_verified:{payload.email}"
    if not await redis_client.exists(verified_key):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP verification required or expired",
            headers={"X-Error-Code": "VERIFICATION_REQUIRED"}
        )
    
    # Find user
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not found",
            headers={"X-Error-Code": "EMAIL_NOT_FOUND"}
        )
    
    # Hash and update password
    user.hashed_password = hash_password(payload.new_password)
    db.commit()
    db.refresh(user)
    
    # Delete verification key
    await redis_client.delete(verified_key)
    
    return {
        "status": True,
        "message": "Password reset successfully"
    }
