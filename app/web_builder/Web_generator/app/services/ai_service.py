"""
AI Service for Groq API Integration
Handles all AI-related API calls for blueprint and code generation using Llama OSS models
"""

import os
import json
import httpx
from typing import Dict, Any, Optional, List
from datetime import datetime
from app.Auth.core.config import get_settings


class AIService:
    """
    Service for interacting with Groq API for content generation.
    Uses Llama OSS models for blueprint and code generation.
    Uses httpx for async HTTP requests.
    """
    
    # Groq API Configuration (hardcoded for reliability)
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"
    GROQ_BLUEPRINT_MODEL = "llama-3.3-70b-versatile"  # OSS model for blueprint/code generation
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize AI Service with Groq API key.
        
        Args:
            api_key: Groq API key. If not provided, reads from environment.
        
        Environment Variables:
            GROQ_API_KEY: API key for Groq
        """
        settings = get_settings()
        self.provider = "groq"
        # Use groq_api_key, fallback to premium_ai_api_key for backward compatibility
        self.api_key = api_key or settings.groq_api_key or settings.premium_ai_api_key
        self.model = self.GROQ_BLUEPRINT_MODEL  # Always use Llama
        self.base_url = self.GROQ_BASE_URL  # Always use Groq API
        self.timeout = 60.0  # seconds
        
        print(f"[AIService] Initialized with model: {self.model}, base_url: {self.base_url}")
        
        # Log warning if API key not found (don't raise error - allow fallback)
        if not self.api_key:
            print("[AIService] WARNING: GROQ_API_KEY not found. AI generation will use fallback.")
    
    def is_available(self) -> bool:
        """Check if AI service is available (has API key)"""
        return bool(self.api_key)
    
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests"""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def _clean_json_response(self, response_text: str) -> str:
        """
        Clean AI response to extract valid JSON.
        Handles markdown code blocks and extra text.
        """
        text = response_text.strip()
        
        # Remove markdown code blocks
        if "```json" in text:
            text = text.split("```json")[-1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[-1].split("```")[0]
        
        text = text.strip()
        
        # Find JSON object boundaries
        start_idx = text.find("{")
        end_idx = text.rfind("}")
        
        if start_idx != -1 and end_idx != -1:
            text = text[start_idx:end_idx + 1]
            
        # Basic cleanup for common AI mistakes
        text = text.replace('\n', ' ')
        
        return text
    
    def generate_content(
        self, 
        system_prompt: str, 
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4000
    ) -> Dict[str, Any]:
        """
        Generate content using AIML API (synchronous).
        
        Args:
            system_prompt: System instructions for the AI
            user_prompt: User prompt with specific request
            temperature: Creativity level (0-1)
            max_tokens: Maximum response tokens
            
        Returns:
            Parsed JSON response from AI
        """
        # Check if API key is available
        if not self.is_available():
            return {"error": "AI service not available - GROQ_API_KEY not set"}
        
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": temperature,
                "max_tokens": max_tokens,
                "response_format": {"type": "json_object"}
            }
            
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self._get_headers(),
                    json=payload
                )
                
                if response.status_code != 200:
                    print(f"[AIService] API Error: {response.status_code} - {response.text}")
                    return {"error": f"API Error: {response.status_code}"}
                
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                
                # Clean and parse JSON
                cleaned_content = self._clean_json_response(content)
                
                try:
                    return json.loads(cleaned_content)
                except json.JSONDecodeError as e:
                    # Log snippet of where it failed
                    error_pos = e.pos
                    snippet = cleaned_content[max(0, error_pos-50):min(len(cleaned_content), error_pos+50)]
                    print(f"[AIService] JSON Parse Error at pos {error_pos}: {e}")
                    print(f"[AIService] Snippet near error: ...{snippet}...")
                    
                    # Try one last resort: removing trailing commas which AI often adds
                    import re
                    try:
                        fixed_content = re.sub(r',\s*([\]}])', r'\1', cleaned_content)
                        return json.loads(fixed_content)
                    except:
                        return {"error": "Failed to parse AI response", "raw_length": len(cleaned_content)}
                    
        except httpx.TimeoutException:
            print("[AIService] Request timeout")
            return {"error": "Request timeout"}
        except Exception as e:
            print(f"[AIService] Error: {str(e)}")
            return {"error": str(e)}
    
    async def generate_content_async(
        self, 
        system_prompt: str, 
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4000
    ) -> Dict[str, Any]:
        """
        Generate content using AIML API (asynchronous).
        
        Args:
            system_prompt: System instructions for the AI
            user_prompt: User prompt with specific request
            temperature: Creativity level (0-1)
            max_tokens: Maximum response tokens
            
        Returns:
            Parsed JSON response from AI
        """
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": temperature,
                "max_tokens": max_tokens,
                "response_format": {"type": "json_object"}
            }
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self._get_headers(),
                    json=payload
                )
                
                if response.status_code != 200:
                    print(f"[AIService] API Error: {response.status_code} - {response.text}")
                    return {"error": f"API Error: {response.status_code}"}
                
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "{}")
                
                # Clean and parse JSON
                cleaned_content = self._clean_json_response(content)
                
                try:
                    return json.loads(cleaned_content)
                except json.JSONDecodeError as e:
                    print(f"[AIService] JSON Parse Error: {e}")
                    return {"error": "Failed to parse AI response", "raw": cleaned_content}
                    
        except httpx.TimeoutException:
            print("[AIService] Request timeout")
            return {"error": "Request timeout"}
        except Exception as e:
            print(f"[AIService] Error: {str(e)}")
            return {"error": str(e)}
    
    def generate_with_retry(
        self,
        system_prompt: str,
        user_prompt: str,
        max_retries: int = 3,
        temperature: float = 0.7,
        max_tokens: int = 4000
    ) -> Dict[str, Any]:
        """
        Generate content with retry logic.
        
        Args:
            system_prompt: System instructions
            user_prompt: User prompt
            max_retries: Maximum retry attempts
            temperature: Creativity level
            max_tokens: Maximum tokens
            
        Returns:
            Parsed JSON response
        """
        last_error = None
        
        for attempt in range(max_retries):
            result = self.generate_content(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            if "error" not in result:
                return result
            
            last_error = result.get("error")
            print(f"[AIService] Attempt {attempt + 1} failed: {last_error}")
            
            # Increase temperature slightly on retry for different results
            temperature = min(temperature + 0.1, 1.0)
        
        return {"error": f"Failed after {max_retries} attempts: {last_error}"}
    
    def validate_blueprint_response(self, response: Dict[str, Any]) -> bool:
        """
        Validate that AI response contains required blueprint fields.
        
        Args:
            response: AI generated blueprint
            
        Returns:
            True if valid, False otherwise
        """
        required_fields = ["projectName", "theme", "components", "navigation"]
        
        if "error" in response:
            return False
            
        for field in required_fields:
            if field not in response:
                print(f"[AIService] Missing required field: {field}")
                return False
        
        # Validate components have required structure
        components = response.get("components", {})
        for comp_key, comp_value in components.items():
            if not isinstance(comp_value, dict):
                continue
            if "type" not in comp_value or "props" not in comp_value:
                print(f"[AIService] Invalid component structure: {comp_key}")
                return False
        
        return True


# Singleton instance
_ai_service_instance: Optional[AIService] = None


def get_ai_service() -> AIService:
    """Get or create AI service singleton instance"""
    global _ai_service_instance
    if _ai_service_instance is None:
        _ai_service_instance = AIService()
    return _ai_service_instance
