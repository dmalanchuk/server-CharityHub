from datetime import datetime, timedelta, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from src.models.login_tokens_model import LoginTokens

class RefreshTokenRepo:

    @staticmethod
    async def safe_refresh_token(user_id: int, refresh_token: str, session: AsyncSession):
        expires_at = datetime.now(timezone.utc) + timedelta(days=30)

        login_token = LoginTokens(
            user_id=user_id,
            refresh_token=refresh_token,
            revoked=False,
            created_at=datetime.now(timezone.utc),
            expires_at=expires_at
        )

        session.add(login_token)
        await session.commit()
