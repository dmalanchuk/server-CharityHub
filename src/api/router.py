from fastapi import APIRouter
from src.api import categories_api, auth_api

router = APIRouter()
router.include_router(categories_api.categories_router, tags=["Categories"])
router.include_router(auth_api.auth_router, tags=["Auth"])
