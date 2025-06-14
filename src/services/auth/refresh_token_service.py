from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.auth.refresh_repo import RefreshTokenRepo


class RefreshTokenService:

    @staticmethod
    async def revoke_refresh_token_service(request, response, session: AsyncSession):
        refresh_token = request.cookies.get("refresh_token")

        await RefreshTokenRepo.revoke_refresh_token(
            refresh_token=refresh_token,
            response=response,
            session=session
        )

        return {"detail": "Refresh token has been revoked"}
