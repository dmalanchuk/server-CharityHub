from typing import Annotated
from pydantic import EmailStr


from sqlalchemy.ext.asyncio import AsyncSession

from src.services.auth.get_info_user_service import GetInfoUserService
from src.services.auth.verification_email_service import VerificationEmailService
from src.services.auth.refresh_token_service import RefreshTokenService
from src.services.auth.login_service import LoginService
from src.schemas.users_schema import CreateUser, LoginUser
from src.database import get_session

from fastapi import APIRouter, Depends, Response, Request

from src.services.auth.registration_service import RegistrationService

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.get("/get/user/{user_id}")
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(get_session)
):
    return await GetInfoUserService.get_user_info_service(user_id, session)

@auth_router.delete("/logout") # logout
async def logout_user(
        request: Request,
        response: Response,
        session: AsyncSession = Depends(get_session)
):
    return await RefreshTokenService.revoke_refresh_token_service(request, response, session)

@auth_router.post("/registration") # registration
async def registration_user(
        data: Annotated[CreateUser, Depends()],
        session: AsyncSession = Depends(get_session)
):
    return await RegistrationService.auth_registration_user_service(data, session)


@auth_router.post("/login/email") # login email
async def login_users_email(
        data: Annotated[LoginUser, Depends()],
        response: Response,
        session: AsyncSession = Depends(get_session)
):
    return await LoginService.login_user_service(data, response, session)

@auth_router.post("/profile/email/get/verification-code")
async def verify_user_email(
        email: EmailStr,
        session: AsyncSession = Depends(get_session)
):
    return await RegistrationService.get_verification_code(email, session)

@auth_router.post("/profile/email/verification")
async def verify_user_email(
        verification_code: str,
        session: AsyncSession = Depends(get_session)
):
    return await VerificationEmailService.verification_email_service(verification_code, session)
