"""
Project Management API endpoints for authenticated users.

This module contains the following endpoints:
- POST /create - Create a new project
- PUT /update/{project_id} - Update project name
- DELETE /delete/{project_id} - Delete a project
- GET /list - List all projects for the user
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.Auth.core.response import success_response, error_response
from app.Auth.db.session import get_db
from app.Auth.core.dependencies import get_current_user
from app.Auth.models.user import User
from app.Auth.models.project import Project
from app.Auth.schemas.project import (
    CreateProjectRequest, UpdateProjectRequest, DeleteProjectRequest,
    CreateProjectResponse, CreateProjectResponseData, UpdateProjectResponse,
    DeleteProjectResponse, ListProjectsResponse,
    SaveProjectRequest, SaveProjectResponse, SaveProjectResponseData,
    ProjectFilesResponse, ProjectDetailsResponse
)

import re
import json
from datetime import datetime, timezone

router = APIRouter(tags=["Project Management"])


@router.post(
    "/project/create",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateProjectResponse,
)
async def create_project(
    payload: CreateProjectRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Create a new project for the authenticated user.
    
    Creates a database record and filesystem folder at:
    Website_builder/backend/{user_id}_{project_id}_{project_name}
    """
    try:
        # Create project in database first to get project_id
        db_project = Project(
            user_id=current_user.user_id,
            project_name=payload.project_name,
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        
        # Create filesystem folder inside projects subfolder
        backend_path = Path(__file__).parent.parent.parent.parent.parent  # Go up to backend folder
        projects_folder = backend_path / "projects"
        projects_folder.mkdir(parents=True, exist_ok=True)
        
        folder_name = f"{current_user.user_id}_{db_project.project_id}_{payload.project_name}"
        project_folder = projects_folder / folder_name
        
        try:
            project_folder.mkdir(parents=True, exist_ok=True)
            
            # Update folder_path in database
            db_project.folder_path = str(project_folder)
            db.commit()
            db.refresh(db_project)
            
        except Exception as folder_error:
            # If folder creation fails, rollback database changes
            db.delete(db_project)
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create project folder: {str(folder_error)}",
                headers={"X-Error-Code": "FOLDER_CREATION_FAILED"}
            )
        
        # Create project data for response
        project_data = CreateProjectResponseData(
            project_id=db_project.project_id
        )
        
        return success_response(
            data=project_data.model_dump(),
            message="Project created successfully"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create project: {str(e)}",
            headers={"X-Error-Code": "PROJECT_CREATION_FAILED"}
        )


@router.put(
    "/project/update",
    status_code=status.HTTP_200_OK,
    response_model=UpdateProjectResponse,
)
async def update_project(
    payload: UpdateProjectRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Update project name for the authenticated user.
    
    Validates ownership, updates database record, and renames the filesystem folder.
    """
    try:
        # Get project and validate ownership
        project = db.query(Project).filter(
            Project.project_id == payload.project_id,
            Project.user_id == current_user.user_id
        ).first()
        
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found or access denied",
                headers={"X-Error-Code": "PROJECT_NOT_FOUND"}
            )
        
        # Store old folder path
        old_folder_path = project.folder_path
        old_project_name = project.project_name
        
        # Update project name in database
        project.project_name = payload.new_project_name
        db.commit()
        db.refresh(project)
        
        # Create new folder path and rename if old folder exists
        if old_folder_path and os.path.exists(old_folder_path):
            backend_path = Path(__file__).parent.parent.parent.parent.parent
            projects_folder = backend_path / "projects"
            projects_folder.mkdir(parents=True, exist_ok=True)
            
            new_folder_name = f"{current_user.user_id}_{project.project_id}_{payload.new_project_name}"
            new_folder_path = projects_folder / new_folder_name
            
            try:
                # Rename the folder
                shutil.move(old_folder_path, new_folder_path)
                
                # Update folder_path in database
                project.folder_path = str(new_folder_path)
                db.commit()
                db.refresh(project)
                
            except Exception as folder_error:
                # If folder rename fails, rollback database changes
                project.project_name = old_project_name
                db.commit()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Failed to rename project folder: {str(folder_error)}",
                    headers={"X-Error-Code": "FOLDER_RENAME_FAILED"}
                )
        else:
            # If old folder doesn't exist, create new folder
            backend_path = Path(__file__).parent.parent.parent.parent.parent
            projects_folder = backend_path / "projects"
            projects_folder.mkdir(parents=True, exist_ok=True)
            
            new_folder_name = f"{current_user.user_id}_{project.project_id}_{payload.new_project_name}"
            new_folder_path = projects_folder / new_folder_name
            
            try:
                new_folder_path.mkdir(parents=True, exist_ok=True)
                project.folder_path = str(new_folder_path)
                db.commit()
                db.refresh(project)
            except Exception as folder_error:
                # Log the error but don't fail the operation
                print(f"Warning: Could not create project folder: {str(folder_error)}")
        
        return {
            "status": True,
            "message": "Project updated successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update project: {str(e)}",
            headers={"X-Error-Code": "PROJECT_UPDATE_FAILED"}
        )


@router.delete(
    "/project/delete",
    status_code=status.HTTP_200_OK,
    response_model=DeleteProjectResponse,
)
async def delete_project(
    payload: DeleteProjectRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Delete a project for the authenticated user.
    
    Validates ownership, deletes database record, and removes the project folder from filesystem.
    """
    try:
        # Get project and validate ownership
        project = db.query(Project).filter(
            Project.project_id == payload.project_id,
            Project.user_id == current_user.user_id
        ).first()
        
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found or access denied",
                headers={"X-Error-Code": "PROJECT_NOT_FOUND"}
            )
        
        # Remove project folder from filesystem if it exists
        if project.folder_path and os.path.exists(project.folder_path):
            try:
                shutil.rmtree(project.folder_path)
            except Exception as folder_error:
                # Log the error but don't fail the operation
                print(f"Warning: Could not remove project folder: {str(folder_error)}")
        
        # Delete project from database
        db.delete(project)
        db.commit()
        
        return {
            "status": True,
            "message": "Project deleted successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete project: {str(e)}",
            headers={"X-Error-Code": "PROJECT_DELETION_FAILED"}
        )


@router.get(
    "/project/list",
    status_code=status.HTTP_200_OK,
    response_model=ListProjectsResponse,
)
async def list_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    List all projects belonging to the authenticated user.
    """
    try:
        # Get all projects for the user
        projects = db.query(Project).filter(
            Project.user_id == current_user.user_id
        ).order_by(Project.created_at.desc()).all()
        
        # Convert to response format (without detailed data)
        projects_list = []
        for project in projects:
            project_data = {
                "project_id": project.project_id,
                "project_name": project.project_name
            }
            projects_list.append(project_data)
        
        return success_response(
            data={"projects": projects_list},
            message="Projects retrieved successfully"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve projects: {str(e)}",
            headers={"X-Error-Code": "PROJECTS_RETRIEVAL_FAILED"}
        )


def _extract_css_js(html_content: str):
    """Simple regex based extraction of CSS and JS from HTML"""
    # Extract CSS from <style> tags
    css_tags = re.findall(r'<style[^>]*>(.*?)</style>', html_content, re.DOTALL)
    css = "\n\n".join(css_tags).strip()
    
    # Extract JS from <script> tags (only those without src)
    js_tags = re.findall(r'<script(?![^>]*src)[^>]*>(.*?)</script>', html_content, re.DOTALL)
    js = "\n\n".join(js_tags).strip()
    
    return css, js


@router.post(
    "/project/save",
    status_code=status.HTTP_200_OK,
    response_model=SaveProjectResponse,
)
async def save_project(
    payload: SaveProjectRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Save project HTML content and metadata to database and filesystem.
    Extracts CSS/JS into separate files and updates progress.
    """
    try:
        # 1. Get project and validate ownership
        # Convert project_id to int if necessary
        pid = int(payload.project_id)
        project = db.query(Project).filter(
            Project.project_id == pid,
            Project.user_id == current_user.user_id
        ).first()
        
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found or access denied",
                headers={"X-Error-Code": "PROJECT_NOT_FOUND"}
            )
        
        # 2. Ensure project folder exists
        if not project.folder_path:
            backend_path = Path(__file__).parent.parent.parent.parent.parent
            projects_folder = backend_path / "projects"
            projects_folder.mkdir(parents=True, exist_ok=True)
            folder_name = f"{current_user.user_id}_{project.project_id}_{project.project_name}"
            project.folder_path = str(projects_folder / folder_name)
        
        project_path = Path(project.folder_path)
        code_path = project_path / "code"
        metadata_path = project_path / "metadata"
        blue_path = project_path / "blue"
        
        code_path.mkdir(parents=True, exist_ok=True)
        metadata_path.mkdir(parents=True, exist_ok=True)
        blue_path.mkdir(parents=True, exist_ok=True)
        
        # 3. Save files to code/ folder
        # Save main index.html
        with open(code_path / "index.html", "w", encoding="utf-8") as f:
            f.write(payload.html_content)
        
        # Extract and save CSS/JS
        css_content, js_content = _extract_css_js(payload.html_content)
        files_created = ["index.html"]
        
        if css_content:
            with open(code_path / "styles.css", "w", encoding="utf-8") as f:
                f.write(css_content)
            files_created.append("styles.css")
            
        if js_content:
            with open(code_path / "script.js", "w", encoding="utf-8") as f:
                f.write(js_content)
            files_created.append("script.js")
            
        # 4. Save metadata/project.json
        now = datetime.now(timezone.utc)
        metadata = {
            "project_id": str(project.project_id),
            "project_name": project.project_name,
            "session_id": payload.session_id,
            "user_id": str(current_user.user_id),
            "last_saved": now.isoformat(),
            "folder_path": project.folder_path
        }
        
        with open(metadata_path / "project.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
            
        # 5. Update database
        project.html_content = payload.html_content
        project.session_id = payload.session_id
        project.last_saved = now
        db.commit()
        db.refresh(project)
        
        return success_response(
            data={
                "project_id": str(project.project_id),
                "folder_path": project.folder_path,
                "files_created": files_created,
                "saved_at": now
            },
            message="Project saved successfully"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to save project: {str(e)}",
            headers={"X-Error-Code": "SAVE_FAILED"}
        )


@router.get(
    "/project/{project_id}/files",
    status_code=status.HTTP_200_OK,
    response_model=ProjectFilesResponse,
)
async def fetch_project_files(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Fetch project files (HTML, CSS, JS).
    Prioritizes filesystem files; falls back to Database content if files/folder are missing.
    """
    try:
        # 1. Get project and validate ownership
        project = db.query(Project).filter(
            Project.project_id == project_id,
            Project.user_id == current_user.user_id
        ).first()
        
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
                headers={"X-Error-Code": "PROJECT_NOT_FOUND"}
            )
            
        files = {"html": "", "css": "", "js": ""}
        metadata = {}
        
        # 2. Try to read from filesystem
        filesystem_read_success = False
        if project.folder_path and os.path.exists(project.folder_path):
            project_path = Path(project.folder_path)
            code_path = project_path / "code"
            metadata_file = project_path / "metadata" / "project.json"
            
            # Read metadata
            if metadata_file.exists():
                try:
                    with open(metadata_file, "r", encoding="utf-8") as f:
                        metadata = json.load(f)
                except Exception:
                    print("Warning: Failed to read metadata.json")

            # Read code files
            if code_path.exists():
                if (code_path / "index.html").exists():
                    with open(code_path / "index.html", "r", encoding="utf-8") as f:
                        files["html"] = f.read()
                        filesystem_read_success = True
                
                if (code_path / "styles.css").exists():
                    with open(code_path / "styles.css", "r", encoding="utf-8") as f:
                        files["css"] = f.read()
                        
                if (code_path / "script.js").exists():
                    with open(code_path / "script.js", "r", encoding="utf-8") as f:
                        files["js"] = f.read()

        # 3. Fallback to DB if filesystem read failed or HTML is empty
        if not files["html"] and project.html_content:
            files["html"] = project.html_content
            # Extract CSS/JS from the DB HTML content so frontend gets consistent structure
            extracted_css, extracted_js = _extract_css_js(project.html_content)
            if not files["css"]:
                files["css"] = extracted_css
            if not files["js"]:
                files["js"] = extracted_js

        return {
            "status": True,
            "message": "Project files fetched successfully",
            "project_id": str(project.project_id),
            "project_name": project.project_name,
            "session_id": project.session_id or metadata.get("session_id", ""),
            "folder_path": project.folder_path or "",
            "last_modified": project.last_saved or project.updated_at,
            "files": files
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch files: {str(e)}",
            headers={"X-Error-Code": "FETCH_FAILED"}
        )


@router.get(
    "/project/{project_id}/details",
    status_code=status.HTTP_200_OK,
    response_model=ProjectDetailsResponse,
)
async def get_project_details(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Get detailed project metadata and status.
    """
    try:
        project = db.query(Project).filter(
            Project.project_id == project_id,
            Project.user_id == current_user.user_id
        ).first()
        
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
                headers={"X-Error-Code": "PROJECT_NOT_FOUND"}
            )
            
        is_saved = project.folder_path is not None and os.path.exists(project.folder_path)
        
        return {
            "status": True,
            "project_id": str(project.project_id),
            "project_name": project.project_name,
            "session_id": project.session_id or "",
            "user_id": str(project.user_id),
            "folder_path": project.folder_path or "",
            "created_at": project.created_at,
            "last_saved": project.last_saved,
            "is_saved_to_folder": is_saved,
            "is_published": False
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get details: {str(e)}",
            headers={"X-Error-Code": "DETAILS_FAILED"}
        )
