from src.schemas.projects_schema import CreateProject

from src.repositories.projects.projects_repo import ProjectsRepository

from sqlalchemy.ext.asyncio import AsyncSession


class ProjectsService:

    @staticmethod
    async def create_project(project: CreateProject, session: AsyncSession):
        project = {
            "title": project.title,
            "description": project.description,
            "category": project.category,
            "goal_amount": project.goal_amount,
            "iban_details": project.iban_details,
            "owner": project.owner,
            "end_date": project.end_date
        }

        return await ProjectsRepository.save_new_projects(project, session)

    @staticmethod
    async def get_all_projects(session: AsyncSession):
        return await ProjectsRepository.get_all_projects(session)
