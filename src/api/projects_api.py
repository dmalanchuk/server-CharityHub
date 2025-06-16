from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session

from fastapi import APIRouter, Depends

from typing import Annotated

projects_router = APIRouter(
    prefix="/projects"
)
