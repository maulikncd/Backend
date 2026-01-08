"""
Standard response helpers to keep API payloads consistent.
"""

from __future__ import annotations

from typing import Any, Dict, Optional


DEFAULT_SUCCESS_MESSAGE = "Operation successful"
DEFAULT_ERROR_CODE = "UNHANDLED_EXCEPTION"


def success_response(
    data: Optional[Dict[str, Any]] = None,
    message: str = DEFAULT_SUCCESS_MESSAGE,
) -> Dict[str, Any]:
    """
    Build the canonical success shape expected by clients.
    """
    return {
        "status": True,
        "message": message,
        "data": data or {},
    }


def error_response(
    message: str,
    error_code: str = DEFAULT_ERROR_CODE,
) -> Dict[str, Any]:
    """
    Build the canonical error shape expected by clients.
    """
    return {
        "status": False,
        "message": message,
        "error_code": error_code,
    }
