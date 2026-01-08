"""
Social authentication API routes for Google login.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from app.Auth.core.response import success_response
from app.Auth.db.session import get_db
from app.Auth.schemas.social import (
    SocialLoginRequest, SocialLoginResponse, SocialLoginResponseData
)
from app.Auth.services.social_service import SocialService

router = APIRouter(tags=["Social Authentication"])


@router.post(
    "/google",
    status_code=status.HTTP_200_OK,
    response_model=SocialLoginResponse,
)
def google_login(
    payload: SocialLoginRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    """
    Authenticate user using Google credentials.
    
    This endpoint supports both:
    1. Existing users (manual signup) logging in with Google
    2. New users creating account with Google
    
    For existing users:
    - Manual username & picture have priority
    - Google data is used as fallback
    - Google social ID is saved if missing
    - "google" is appended to login_method
    
    For new users:
    - Account is created with Google data
    - login_method is set to "google"
    - Account is marked as verified
    """
    # Force login_method to be "google" for this endpoint
    payload.login_method = "google"
    
    social_service = SocialService()
    login_data = social_service.login(
        db,
        email=payload.email,
        username=payload.username,
        login_method=payload.login_method,
        social_id=payload.social_id,
        picture=payload.picture,
        device_id=payload.device_id,
        device_name=payload.device_name,
        location=payload.location,
        ip_address=request.client.host if request.client else None,
    )

    response_data = SocialLoginResponseData(**login_data)
    return success_response(data=response_data.model_dump(), message="Login successful")
