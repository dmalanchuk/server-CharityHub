from datetime import datetime, timedelta, timezone

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Response, HTTPException

from src.models.login_tokens_model import LoginTokens


class RefreshTokenRepo:

    @staticmethod
    async def safe_refresh_token(user_id: int, refresh_token: str, session: AsyncSession):
        aware_created_at = datetime.now(timezone.utc)
        aware_expires_at = aware_created_at + timedelta(days=30)

        created_at = aware_created_at.replace(tzinfo=None)
        expires_at = aware_expires_at.replace(tzinfo=None)

        login_token = LoginTokens(
            user_id=user_id,
            refresh_token=refresh_token,
            revoked=False,
            created_at=created_at,
            expires_at=expires_at
        )

        session.add(login_token)
        await session.commit()

    @staticmethod
    async def revoke_refresh_token(refresh_token: str, response: Response, session: AsyncSession):
        if not refresh_token:
            raise HTTPException(status_code=401, detail="Refresh token is required")

        await session.execute(
            LoginTokens.__table__.update().where(LoginTokens.refresh_token == refresh_token).values(revoked=True)
        )

        await session.commit()
        response.delete_cookie("refresh_token")
