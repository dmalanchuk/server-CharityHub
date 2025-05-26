from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.repositories.categories_repo import CategoriesRepository
from src.services.categories_service import CategoriesService
from src.schemas.categories_schema import CategoryBase

categories_router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)


@categories_router.get("/")
async def get_categories(
    session: AsyncSession = Depends(get_session)
):
    return await CategoriesRepository.get_all(session)


@categories_router.post("/")
async def post_categories(
        data: CategoryBase,
        session: AsyncSession = Depends(get_session)
):
   return await CategoriesService.create_category(session, data)
