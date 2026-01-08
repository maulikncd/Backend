"""
Change Password API for authenticated users to update their password.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, validator
from sqlalchemy.orm import Session

from app.Auth.core.response import success_response
from app.Auth.core.security import verify_password, hash_password
from app.Auth.core.dependencies import get_current_user
from app.Auth.crud.auth import get_user_by_email
from app.Auth.crud.refresh_token import revoke_user_refresh_tokens
from app.Auth.db.session import get_db
from app.Auth.models.user import User

router = APIRouter(tags=["Change Password"])

# Schemas
class ChangePasswordRequest(BaseModel):
    """Schema for change password request."""
    old_password: str = Field(..., description="Current password")
    new_password: str = Field(..., description="New password (min 6 characters)")
    confirm_password: str = Field(..., description="Confirm new password")
    
    @validator('new_password')
    def validate_new_password(cls, v):
        if not v or not v.strip():
            raise ValueError('New password cannot be empty')
        if len(v.strip()) < 6:
            raise ValueError('New password must be at least 6 characters long')
        return v
    
    @validator('confirm_password')
    def validate_confirm_password(cls, v):
        if not v or not v.strip():
            raise ValueError('Confirm password cannot be empty')
        return v


@router.post(
    "/change-password",
    status_code=status.HTTP_200_OK,
)
async def change_password(
    payload: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Change password for authenticated user.
    
    Rules:
    - Require valid access token
    - Verify old_password with stored hashed password
    - Validate new_password == confirm_password
    - Hash and update new password in DB
    - Invalidate existing refresh tokens
    """
    
    # Validate new passwords match
    if payload.new_password != payload.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New passwords do not match",
            headers={"X-Error-Code": "PASSWORDS_MISMATCH"}
        )
    
    # Validate old password
    if not verify_password(payload.old_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect",
            headers={"X-Error-Code": "INVALID_OLD_PASSWORD"}
        )
    
    # Validate new password is different from old password
    if verify_password(payload.new_password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password must be different from current password",
            headers={"X-Error-Code": "SAME_PASSWORD"}
        )
    
    # Hash and update new password
    current_user.hashed_password = hash_password(payload.new_password)
    db.commit()
    db.refresh(current_user)
    
    # Invalidate all existing refresh tokens for this user
    revoked_tokens = revoke_user_refresh_tokens(db, current_user.user_id)
    
    return {
        "status": True,
        "message": "Password changed successfully"
    }
