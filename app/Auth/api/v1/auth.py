"""
Auth API routes for user authentication.

This module contains the following endpoints:
- POST /signup - Create a new user account
- POST /login - Authenticate a user and get access/refresh tokens
- POST /logout - Invalidate the current refresh token
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.Auth.core.response import success_response, error_response
from app.Auth.db.session import get_db
from app.Auth.schemas.auth import (
    SignupRequest, SignupResponse, SignupResponseData,
    OTPRequest, OTPResponse, OTPVerifyRequest, OTPVerifyResponse, OTPVerifyResponseData,
    OTPVerifyOnlyResponse,
    SignupSchema, VerifyOTPSchema
)
from app.Auth.schemas.login import LoginRequest, LoginResponse, LoginResponseData
from app.Auth.schemas.token import LogoutRequest, LogoutResponse, LogoutResponseData
from app.Auth.services.auth_service import AuthService
from app.Auth.services.login_service import LoginService
from app.Auth.services.logout_service import LogoutService

router = APIRouter(tags=["Authentication"])


@router.post(
    "/signup",
    status_code=status.HTTP_200_OK,
    response_model=OTPResponse,
)
async def signup_user(
    payload: SignupRequest,  # Accepts SignupSchema alias as well
    db: Session = Depends(get_db),
):
    """Send OTP for email verification during signup and store user data."""
    auth_service = AuthService()
    await auth_service.send_signup_otp(
        db, 
        email=payload.email,
        username=payload.username,
        password=payload.password,
        confirm_password=payload.confirm_password,
        login_method=payload.login_method,
        device_id=payload.device_id,
        device_name=payload.device_name,
        location=payload.location,
    )
    
    return success_response(data={}, message="OTP sent successfully")


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=LoginResponse,
)
def login_user(
    payload: LoginRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    login_service = LoginService()
    login_data = login_service.login(
        db,
        email=payload.email,
        password=payload.password,
        login_method=payload.login_method,
        device_id=payload.device_id,
        device_name=payload.device_name,
        location=payload.location,
        ip_address=request.client.host if request.client else None,
    )

    response_data = LoginResponseData(**login_data)
    return success_response(data=response_data.model_dump(), message="Login successful")


@router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
    responses={
        400: {"description": "Invalid or expired token"},
        401: {"description": "Could not validate credentials"},
    },
)
async def logout(
    request: Request,
    db: Session = Depends(get_db),
):
    """
    Logout user by invalidating the refresh token and blacklisting access token.
    
    Expects:
    - Authorization header with refresh token (Bearer <refresh_token>)
    - X-Access-Token header with access token (optional, for immediate blacklisting)
    """
    try:
        # Get the refresh token from Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=error_response(
                    message="Missing or invalid Authorization header",
                    error_code="MISSING_TOKEN"
                )
            )
        
        refresh_token = auth_header.split(" ")[1]
        
        # Get access token from X-Access-Token header (optional)
        access_token = request.headers.get("X-Access-Token")
        
        # Fallback: try to get access token from Authorization header if it's an access token
        if not access_token:
            try:
                from jose import jwt
                from app.Auth.core.config import get_settings
                settings = get_settings()
                
                # Try to decode the token from Authorization header
                potential_access_token = refresh_token  # This is actually the token from Authorization header
                payload = jwt.decode(
                    potential_access_token,
                    settings.access_token_secret,
                    algorithms=[settings.jwt_algorithm],
                )
                
                # If it has jti claim and no type=refresh, it's likely an access token
                if payload.get("jti") and payload.get("type") != "refresh":
                    access_token = potential_access_token
                    logger.info("Using access token from Authorization header as fallback")
                    
            except Exception:
                # Not an access token, continue with refresh token logic
                pass
        
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"Logout request - refresh_token present: {bool(refresh_token)}, access_token present: {bool(access_token)}")
        if access_token:
            logger.info(f"Access token (first 20 chars): {access_token[:20]}...")
        
        # Use the logout service to handle the logout logic
        logout_data = LogoutService.logout(
            db=db,
            refresh_token=refresh_token,
            access_token=access_token,
            ip_address=request.client.host if request.client else None,
        )
        
        return {
            "status": "success",
            "message": "Logged out successfully"
        }
        
    except Exception as e:
        # Handle different types of token errors
        error_message = str(e).lower()
        
        if "expired" in error_message:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=error_response(
                    message="Refresh token has expired",
                    error_code="TOKEN_EXPIRED"
                )
            )
            
        elif "invalid" in error_message or "hash" in error_message:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=error_response(
                    message="Invalid refresh token",
                    error_code="INVALID_TOKEN"
                )
            )
            
        elif "already logged out" in error_message:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=error_response(
                    message="Already logged out",
                    error_code="ALREADY_LOGGED_OUT"
                )
            )
        
        # For any other unexpected errors
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=error_response(
                message="An error occurred while logging out",
                error_code="INTERNAL_SERVER_ERROR"
            )
        )


@router.post(
    "/verify-otp",
    status_code=status.HTTP_201_CREATED,
    response_model=OTPVerifyResponse,
)
async def verify_signup_otp(
    payload: OTPVerifyRequest,  # Accepts VerifyOTPSchema alias as well
    request: Request,
    db: Session = Depends(get_db),
):
    """Verify OTP and create user account using stored user data."""
    auth_service = AuthService()
    signup_data = await auth_service.verify_otp_only(
        db,
        email=payload.email,
        otp=payload.otp,
        ip_address=request.client.host if request.client else None,
    )

    response_data = OTPVerifyResponseData(**signup_data)
    return success_response(data=response_data.model_dump(), message="Account created successfully!")
