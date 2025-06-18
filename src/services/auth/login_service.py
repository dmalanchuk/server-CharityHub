from sqlalchemy.ext.asyncio import AsyncSession

from src.core.token_utils import create_access_token, create_refresh_token
from src.schemas.users_schema import LoginUser
from src.repositories.auth.login_user_repo import LoginUserRepo
from src.repositories.auth.refresh_repo import RefreshTokenRepo

from fastapi import Response


class LoginService:

    @staticmethod
    async def login_user_service(data: LoginUser, response: Response, session: AsyncSession):
        user = await LoginUserRepo.auth_user(data.email, data.password, session)

        access_token = create_access_token(
            data={"sub": data.email},
        )
        refresh_token = create_refresh_token(
            data={"sub": data.email},
        )

        await RefreshTokenRepo.safe_refresh_token(user.id, refresh_token, session)

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=False, # для тестування локально, потім змінити на True
            samesite="Lax",
            max_age=3600 * 24 * 30,
        )

        return {"access_token": access_token}
