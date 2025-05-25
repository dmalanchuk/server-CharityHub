from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session


class CategoriesRepository:

    @staticmethod
    async def get_session():
        ...
