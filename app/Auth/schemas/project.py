"""
Pydantic schemas for project management endpoints.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Dict

from pydantic import BaseModel, Field, field_validator
import re


class CreateProjectRequest(BaseModel):
    """Schema for creating a new project."""
    project_name: str = Field(..., min_length=1, max_length=255, description="Project name")
    
    @field_validator("project_name")
    @classmethod
    def sanitize_project_name(cls, value: str) -> str:
        """Sanitize project name for filesystem usage."""
        if not value or not value.strip():
            raise ValueError("Project name cannot be empty")
        
        # Remove invalid filesystem characters
        sanitized = re.sub(r'[<>:"/\\|?*]', '', value.strip())
        
        # Replace spaces with underscores and convert to lowercase
        sanitized = re.sub(r'\s+', '_', sanitized.lower())
        
        # Remove consecutive underscores
        sanitized = re.sub(r'_+', '_', sanitized)
        
        # Remove leading/trailing underscores
        sanitized = sanitized.strip('_')
        
        if not sanitized:
            raise ValueError("Project name contains only invalid characters")
        
        if len(sanitized) > 100:
            raise ValueError("Sanitized project name is too long")
        
        return sanitized


class UpdateProjectRequest(BaseModel):
    """Schema for updating a project name."""
    project_id: int = Field(..., description="Project ID to update")
    new_project_name: str = Field(..., min_length=1, max_length=255, description="New project name")
    
    @field_validator("new_project_name")
    @classmethod
    def sanitize_project_name(cls, value: str) -> str:
        """Sanitize project name for filesystem usage."""
        if not value or not value.strip():
            raise ValueError("Project name cannot be empty")
        
        # Remove invalid filesystem characters
        sanitized = re.sub(r'[<>:"/\\|?*]', '', value.strip())
        
        # Replace spaces with underscores and convert to lowercase
        sanitized = re.sub(r'\s+', '_', sanitized.lower())
        
        # Remove consecutive underscores
        sanitized = re.sub(r'_+', '_', sanitized)
        
        # Remove leading/trailing underscores
        sanitized = sanitized.strip('_')
        
        if not sanitized:
            raise ValueError("Project name contains only invalid characters")
        
        if len(sanitized) > 100:
            raise ValueError("Sanitized project name is too long")
        
        return sanitized


class DeleteProjectRequest(BaseModel):
    """Schema for deleting a project."""
    project_id: int = Field(..., description="Project ID to delete")


class CreateProjectResponseData(BaseModel):
    """Schema for create project response data."""
    project_id: int


class CreateProjectResponse(BaseModel):
    """Schema for create project response."""
    status: bool = True
    message: str = Field(default="Project created successfully")
    data: CreateProjectResponseData


class UpdateProjectResponse(BaseModel):
    """Schema for update project response."""
    status: bool = True
    message: str = Field(default="Project updated successfully")


class DeleteProjectResponse(BaseModel):
    """Schema for delete project response."""
    status: bool = True
    message: str = Field(default="Project deleted successfully")


class ListProjectsResponse(BaseModel):
    """Schema for list projects response."""
    status: bool = True
    message: str = Field(default="Projects retrieved successfully")
    data: dict = Field(default={"projects": []})


# --- New schemas for Save/Fetch Project ---

from typing import Optional, List, Dict, Union

# ... (existing imports)

class SaveProjectRequest(BaseModel):
    """Schema for saving project to database and folder."""
    session_id: str = Field(..., description="Interview Session ID")
    project_id: Union[str, int] = Field(..., description="Project ID")
    project_name: str = Field(..., description="Project Name")
    html_content: str = Field(..., description="Full HTML content of the website")

class SaveProjectResponseData(BaseModel):
    project_id: str
    folder_path: str
    files_created: List[str]
    saved_at: datetime

class SaveProjectResponse(BaseModel):
    status: bool = True
    message: str = "Project saved successfully"
    data: SaveProjectResponseData

class ProjectFilesResponse(BaseModel):
    status: bool = True
    message: str = "Project files fetched successfully"
    project_id: str
    project_name: str
    session_id: str
    folder_path: str
    last_modified: datetime
    files: Dict[str, str]

class ProjectDetailsResponse(BaseModel):
    status: bool = True
    project_id: str
    project_name: str
    session_id: str
    user_id: str
    folder_path: str
    created_at: datetime
    last_saved: Optional[datetime]
    is_saved_to_folder: bool
    is_published: bool
