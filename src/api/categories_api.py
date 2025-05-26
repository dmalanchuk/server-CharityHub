from fastapi import APIRouter, Depends, HTTPException
from src.schemas.categories_schema import CategoryBase

categories_router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)


@categories_router.get("/")
async def get_categories(

) -> list[CategoryBase]:
    ...


@categories_router.post("/")
async def post_categories(
        category: CategoryBase
):
   ...
