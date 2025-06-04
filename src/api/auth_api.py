from typing import Annotated
from pydantic import EmailStr


from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session

from fastapi import APIRouter, Depends

from src.services.auth.registration_service import RegistrationService

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.post("/registration") # registration
async def registration_user(
        username: str,
        email: str,
        password: str,
        session: AsyncSession = Depends(get_session)
):
    ...


@auth_router.post("/login/email") # login email
async def login_users(
        email: str,
        password: str,
        session: AsyncSession = Depends(get_session)
):
    ...


@auth_router.post("/login/username") # login username
async def login_users(
        username: str,
        password: str,
        session: AsyncSession = Depends(get_session)
):
    ...


@auth_router.delete("/logout") # logout
async def logout_user(
        session: AsyncSession = Depends(get_session)
):
    ...


@auth_router.post("/profile/email/verify")
async def verify_user(
        email: EmailStr,
        session: AsyncSession = Depends(get_session)
):
    return await RegistrationService.get_verification_code(email, session)
