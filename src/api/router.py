from fastapi import APIRouter
from src.api import categories_api

router = APIRouter()
router.include_router(categories_api.categories_router, tags=["Categories"])
