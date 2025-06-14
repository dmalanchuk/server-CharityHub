from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users_model import UserModel


class GetVerifyCodeRepo:

    @staticmethod
    async def get_verification_code_db(code: str, session: AsyncSession):
        stmt = select(UserModel.verified_code).where(UserModel.verified_code == code)
        result = await session.execute(stmt)
        verif_code = result.scalar_one_or_none()

        if verif_code is None:
            raise HTTPException(status_code=404, detail="User did not send verification code")

        return verif_code
