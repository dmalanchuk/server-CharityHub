from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.categories_model import CategoriesModel
from src.schemas.categories_schema import CategoryBase


class CategoriesRepository:

    @staticmethod
    async def get_all(session: AsyncSession):
        result = await session.execute(select(CategoriesModel))
        return result.scalars().all()


    @staticmethod
    async def create(session: AsyncSession, data: CategoryBase):
        category = CategoriesModel(**data.to_dict())
        data.session.add(category)
        await data.session.commit()
        await data.session.refresh(category)
        return category
