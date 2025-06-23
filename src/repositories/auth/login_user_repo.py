from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.security_pw import pwd_context
from src.models.users_model import UserModel
from sqlalchemy import select


class LoginUserRepo:

    @classmethod
    async def auth_user(cls, email: str, password: str, session: AsyncSession):
        result = await session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=401, detail="This email is no registered or entered incorrectly")
        if not pwd_context.verify(password, user.password):
            raise HTTPException(status_code=401, detail="This password is incorrect")
        return user
