"""
OTP utility functions for email verification using Redis.
"""

from __future__ import annotations

import random
import string
import json
from typing import Optional, Dict, Any

import redis.asyncio as redis
import aiosmtplib
from email.message import EmailMessage

from app.Auth.core.config import get_settings


class OTPService:
    """
    Service for generating, storing, and verifying OTPs using Redis.
    """
    
    @staticmethod
    def generate_otp(length: int = 6) -> str:
        """Generate a numeric OTP of specified length."""
        return ''.join(random.choices(string.digits, k=length))
    
    @staticmethod
    async def get_redis_client() -> redis.Redis:
        """Get Redis client instance."""
        settings = get_settings()
        return redis.from_url(settings.redis_url, decode_responses=True)
    
    @staticmethod
    async def store_otp(email: str, otp: str) -> bool:
        """
        Store OTP in Redis with TTL.
        
        Args:
            email: User's email address
            otp: Generated OTP
            
        Returns:
            True if stored successfully, False if OTP already exists
        """
        redis_client = await OTPService.get_redis_client()
        settings = get_settings()
        
        key = f"signup_otp:{email}"
        
        # Check if OTP already exists
        if await redis_client.exists(key):
            return False
        
        # Store OTP with TTL
        await redis_client.setex(
            key,
            settings.otp_ttl_minutes * 60,  # Convert minutes to seconds
            otp
        )
        
        return True
    
    @staticmethod
    async def verify_otp(email: str, provided_otp: str) -> bool:
        """
        Verify OTP against stored value.
        
        Args:
            email: User's email address
            provided_otp: OTP provided by user
            
        Returns:
            True if OTP matches, False otherwise
        """
        redis_client = await OTPService.get_redis_client()
        key = f"signup_otp:{email}"
        
        stored_otp = await redis_client.get(key)
        
        if stored_otp is None:
            return False
        
        if stored_otp == provided_otp:
            # Delete the OTP after successful verification
            await redis_client.delete(key)
            return True
        
        return False
    
    @staticmethod
    async def send_otp_email(email: str, otp: str) -> bool:
        """
        Send OTP to user's email address.
        
        Args:
            email: User's email address
            otp: Generated OTP
            
        Returns:
            True if email sent successfully, False otherwise
        """
        settings = get_settings()

        if not settings.smtp_enabled:
            # Log OTP for development/testing when SMTP is disabled
            print(f"WARNING: SMTP is disabled. OTP for {email} is: {otp}")
            return True

        try:
            message = EmailMessage()
            message["From"] = settings.smtp_username
            message["To"] = email
            message["Subject"] = "Your OTP for Website Builder Signup"
            
            body = f"""
            Your 6-digit OTP for Website Builder signup is: {otp}
            
            This OTP will expire in {settings.otp_ttl_minutes} minute(s).
            
            If you didn't request this OTP, please ignore this email.
            """
            
            message.set_content(body)
            
            await aiosmtplib.send(
                message,
                hostname=settings.smtp_host,
                port=settings.smtp_port,
                username=settings.smtp_username,
                password=settings.smtp_password,
                start_tls=True,  # Use STARTTLS for port 587
                timeout=10.0,
            )
            
            return True
            
        except Exception as e:
            # Log the actual error for debugging
            print(f"SMTP Error: {str(e)}")
            print(f"SMTP Config: Host={settings.smtp_host}, Port={settings.smtp_port}, Username={settings.smtp_username}")
            return False

    @staticmethod
    async def store_user_data(email: str, user_data: Dict[str, Any]) -> bool:
        """
        Store user data in Redis with TTL.
        
        Args:
            email: User's email address
            user_data: Dictionary containing user registration data
            
        Returns:
            True if stored successfully
        """
        redis_client = await OTPService.get_redis_client()
        settings = get_settings()
        
        key = f"signup_data:{email}"
        
        # Store user data as JSON with TTL
        await redis_client.setex(
            key,
            settings.otp_ttl_minutes * 60,  # Use same TTL as OTP
            json.dumps(user_data)
        )
        
        return True
    
    @staticmethod
    async def get_user_data(email: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve stored user data from Redis.
        
        Args:
            email: User's email address
            
        Returns:
            User data dictionary if found, None otherwise
        """
        redis_client = await OTPService.get_redis_client()
        key = f"signup_data:{email}"
        
        stored_data = await redis_client.get(key)
        
        if stored_data is None:
            return None
        
        try:
            return json.loads(stored_data)
        except json.JSONDecodeError:
            return None
    
    @staticmethod
    async def send_forgot_password_otp(email: str, otp: str) -> bool:
        """
        Send OTP to user's email address for password reset.
        
        Args:
            email: User's email address
            otp: Generated OTP
            
        Returns:
            True if email sent successfully, False otherwise
        """
        settings = get_settings()
        
        try:
            message = EmailMessage()
            message["From"] = settings.smtp_username
            message["To"] = email
            message["Subject"] = "Your OTP for Website Builder Password Reset"
            
            body = f"""
            Your 6-digit OTP for Website Builder password reset is: {otp}
            
            This OTP will expire in 1 minute.
            
            If you didn't request this OTP, please ignore this email.
            """
            
            message.set_content(body)
            
            await aiosmtplib.send(
                message,
                hostname=settings.smtp_host,
                port=settings.smtp_port,
                username=settings.smtp_username,
                password=settings.smtp_password,
                start_tls=True,  # Use STARTTLS for port 587
                timeout=10.0,
            )
            
            return True
            
        except Exception as e:
            # Log the actual error for debugging
            print(f"SMTP Error: {str(e)}")
            print(f"SMTP Config: Host={settings.smtp_host}, Port={settings.smtp_port}, Username={settings.smtp_username}")
            return False

    @staticmethod
    async def delete_user_data(email: str) -> bool:
        """
        Delete stored user data from Redis.
        
        Args:
            email: User's email address
            
        Returns:
            True if deleted successfully
        """
        redis_client = await OTPService.get_redis_client()
        key = f"signup_data:{email}"
        
        result = await redis_client.delete(key)
        return result > 0