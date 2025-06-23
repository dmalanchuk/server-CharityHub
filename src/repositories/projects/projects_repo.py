from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.projects_model import ProjectsModel


class ProjectsRepository:

    @staticmethod
    async def save_new_projects(project: dict, session: AsyncSession, ):
        new_project = ProjectsModel(**project)

        session.add(new_project)
        await session.commit()
        await session.refresh(new_project)

        return new_project

    @staticmethod
    async def get_all_projects(session: AsyncSession):
        res = await session.execute(select(ProjectsModel))
        return res.scalars().all()
