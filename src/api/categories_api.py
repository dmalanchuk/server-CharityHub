from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session


categories_router = APIRouter(
    tags=["categories"]
)


@categories_router.get("/")
async def get_categories(session: AsyncSession = Depends(get_session)):
    pass


@categories_router.post("/")
async def post_categories():
    pass
