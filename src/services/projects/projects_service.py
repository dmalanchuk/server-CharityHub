from src.schemas.projects_schema import CreateProject

from src.repositories.projects.projects_repo import ProjectsRepository

from sqlalchemy.ext.asyncio import AsyncSession


class ProjectsService:

    @staticmethod
    async def create_project(project: CreateProject, session: AsyncSession):

        project = {
            "title": project.title,
            "description": project.description,
            "category_id": project.category_id,
            "goal_amount": project.goal_amount,
            "url_donations": project.url_donations,
            "owner": project.owner,
            "end_date": project.end_date
        }

        return await ProjectsRepository.save_new_projects(project, session)
