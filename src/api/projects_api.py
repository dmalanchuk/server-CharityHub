from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.get_current_user import get_current_user
from src.schemas.projects_schema import CreateProject
from src.services.projects.projects_service import ProjectsService
from src.database import get_session

from fastapi import APIRouter, Depends


projects_router = APIRouter(
    prefix="/projects"
)

@projects_router.post("/create/project")
async def create_project(
    data: CreateProject,
    current_user = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    return await ProjectsService.create_project(data, current_user, session)
