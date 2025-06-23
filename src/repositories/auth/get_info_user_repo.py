from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users_model import UserModel


class GetInfoUserRepo:

    @staticmethod
    async def get_user_info(user_id: int, session: AsyncSession):
        res = await session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        result = res.scalars().first()

        if not result:
            raise HTTPException(status_code=404, detail="User not found")

        full_result = {
            "username": result.username,
            "email": result.email,
            "is_verified": result.is_verified
        }

        return full_result
