from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.categories_repo import CategoriesRepository
from src.schemas.categories_schema import CategoryBase


class CategoriesService:

    @staticmethod
    async def create_category(session: AsyncSession, category: CategoryBase):
        return await CategoriesRepository.create(session, category)


    @staticmethod
    async def get_all_categories(session: AsyncSession):
        return await CategoriesRepository.get_all(session)
