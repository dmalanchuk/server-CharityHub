from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session
from src.schemas.categories_schema import CategoryBase


class CategoriesRepository:

    @staticmethod
    async def get_all() -> list[CategoryBase]:
        ...


    @staticmethod
    async def create() -> CategoryBase:
        ...
