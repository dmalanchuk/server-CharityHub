from fastapi import APIRouter
from src.api import categories_api, auth_api, projects_api

router = APIRouter()
router.include_router(categories_api.categories_router, tags=["Categories"])
router.include_router(auth_api.auth_router, tags=["Auth"])
router.include_router(projects_api.projects_router, tags=["Projects"])
