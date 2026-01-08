"""
Utility functions for Web_generator module
# added by web_generator
"""

import re
import json
from typing import Dict, Any, List, Optional
from datetime import datetime

def validate_session_id(session_id: str) -> bool:
    """Validate session ID format"""
    return isinstance(session_id, str) and len(session_id) > 0

def sanitize_code(code: str) -> str:
    """Sanitize generated code to prevent security issues"""
    # Remove potentially dangerous patterns
    dangerous_patterns = [
        r'<script[^>]*>.*?</script>',
        r'javascript:',
        r'on\w+\s*=',
    ]
    
    for pattern in dangerous_patterns:
        code = re.sub(pattern, '', code, flags=re.IGNORECASE | re.DOTALL)
    
    return code

def format_timestamp(timestamp: Optional[str] = None) -> str:
    """Format timestamp for display"""
    if timestamp:
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            pass
    
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def extract_file_extension(file_path: str) -> str:
    """Extract file extension from file path"""
    return file_path.split('.')[-1].lower() if '.' in file_path else ''

def validate_file_path(file_path: str) -> bool:
    """Validate file path for security"""
    # Prevent directory traversal
    if '..' in file_path or file_path.startswith('/'):
        return False
    
    # Allow only specific file extensions
    allowed_extensions = ['html', 'css', 'js', 'json', 'txt']
    extension = extract_file_extension(file_path)
    
    return extension in allowed_extensions

def generate_component_name(component_type: str) -> str:
    """Generate component name based on type"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{component_type}_{timestamp}"

def parse_requirements(requirements: Dict[str, Any]) -> List[str]:
    """Parse requirements into list of strings"""
    if not requirements:
        return []
    
    parsed = []
    for key, value in requirements.items():
        if isinstance(value, str):
            parsed.append(f"{key}: {value}")
        elif isinstance(value, list):
            parsed.append(f"{key}: {', '.join(map(str, value))}")
        elif isinstance(value, dict):
            parsed.append(f"{key}: {json.dumps(value)}")
    
    return parsed

def create_error_response(message: str, status_code: int = 400) -> Dict[str, Any]:
    """Create standardized error response"""
    return {
        "error": True,
        "message": message,
        "status_code": status_code,
        "timestamp": datetime.now().isoformat()
    }

def create_success_response(data: Any, message: str = "Success") -> Dict[str, Any]:
    """Create standardized success response"""
    return {
        "error": False,
        "message": message,
        "data": data,
        "timestamp": datetime.now().isoformat()
    }
