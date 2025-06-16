from sqlalchemy.ext.asyncio import AsyncSession

from src.models.projects_model import ProjectsModel
from src.schemas.projects_schema import CreateProject

class ProjectsRepository:

    @staticmethod
    async def save_new_projects(project: CreateProject, session: AsyncSession,):
        new_project = ProjectsModel(**project)

        session.add(new_project)
        await session.commit()
        await session.refresh(new_project)
