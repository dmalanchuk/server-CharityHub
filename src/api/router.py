from fastapi import APIRouter
from src.api import auth_api, projects_api

router = APIRouter()
router.include_router(auth_api.auth_router, tags=["Auth"])
router.include_router(projects_api.projects_router, tags=["Projects"])
