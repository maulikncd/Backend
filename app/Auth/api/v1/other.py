"""
Refresh token API routes.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.Auth.core.response import success_response, error_response
from app.Auth.db.session import get_db
from app.Auth.schemas.token import TokenResponse, TokenResponseData
from app.Auth.services.refresh_token_service import RefreshTokenService
from app.Auth.core.dependencies import get_current_user
from app.Auth.models.user import User
from pydantic import BaseModel
from typing import Optional


# Schema for user info response
class UserInfoResponseData(BaseModel):
    user_id: int
    username: str
    email: str
    picture: Optional[str] = None


class UserInfoResponse(BaseModel):
    status: bool = True
    message: str = "User information retrieved successfully"
    data: UserInfoResponseData


router = APIRouter(tags=["Auth"])

@router.post(
    "/refresh",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
    responses={
        400: {"description": "Invalid or expired token"},
        401: {"description": "Could not validate credentials"},
    },
)
async def refresh_token(
    request: Request,
    db: Session = Depends(get_db),
):
    """
    Refresh access token using a valid refresh token from Authorization header.
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
        
        # Use the refresh token service to handle the refresh logic
        token_data = RefreshTokenService.refresh_token(
            db=db,
            refresh_token=refresh_token,
        )

        response_data = TokenResponseData(
            access_token=token_data["access_token"],
            refresh_token=token_data["refresh_token"],
        )

        return {
            "status": "success",
            "message": "Token refreshed successfully",
            "data": response_data.model_dump()
        }

    except Exception as e:
        error_message = str(e).lower()

        if "expired" in error_message:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=error_response(
                    message="Refresh token has expired",
                    error_code="TOKEN_EXPIRED"
                )
            )

        if "invalid" in error_message or "hash" in error_message:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=error_response(
                    message="Invalid refresh token",
                    error_code="INVALID_TOKEN"
                )
            )

        if "inactive" in error_message:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=error_response(
                    message="Refresh token is no longer valid",
                    error_code="TOKEN_INACTIVE"
                )
            )

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=error_response(
                message="An error occurred while refreshing the token",
                error_code="INTERNAL_SERVER_ERROR"
            )
        )


@router.get(
    "/user-info",
    status_code=status.HTTP_200_OK,
    response_model=UserInfoResponse,
    responses={
        401: {"description": "Invalid or expired token"},
        404: {"description": "User not found"},
    },
)
async def get_user_info(
    current_user: User = Depends(get_current_user),
):
    """
    Get current user information using a valid access token.
    
    This endpoint validates the access token from the Authorization header
    and returns the user's profile information.
    
    Headers required:
    - Authorization: Bearer <access_token>
    
    Returns:
    - User profile information including ID, username, email, login method, etc.
    """
    try:
        user_data = UserInfoResponseData(
            user_id=current_user.user_id,
            username=current_user.username,
            email=current_user.email,
            picture=current_user.picture,
        )
        
        response_data = UserInfoResponse(
            status=True,
            message="User information retrieved successfully",
            data=user_data
        )
        
        return response_data
        
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=error_response(
                message="An error occurred while retrieving user information",
                error_code="INTERNAL_SERVER_ERROR"
            )
        )
