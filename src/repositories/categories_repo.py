from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.categories_model import CategoriesModel
from src.schemas.categories_schema import CategoryBase


class CategoriesRepository:

    @classmethod
    async def get_all(cls, session: AsyncSession):
        result = await session.execute(select(CategoriesModel))
        return result.scalars().all()


    @classmethod
    async def create(cls, session: AsyncSession, data: CategoryBase):
        category = CategoriesModel(**data.model_dump())
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category
