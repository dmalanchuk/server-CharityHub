from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.projects_schema import CreateProject
from src.services.projects.projects_service import ProjectsService
from src.database import get_session

from fastapi import APIRouter, Depends

from typing import Annotated

projects_router = APIRouter(
    prefix="/projects"
)

@projects_router.post("/create/project")
async def create_project(
    data: Annotated[CreateProject, Depends()],
    session: AsyncSession = Depends(get_session)
):
    return await ProjectsService.create_project(data ,session)
