from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.auth.get_verify_code_repo import GetVerifyCodeRepo
from src.models.users_model import UserModel


class VerificationEmailService:

    @staticmethod
    async def verification_email_service(ver_code: str, session: AsyncSession):
        saved_code = await GetVerifyCodeRepo.get_verification_code_db(ver_code, session)

        if saved_code and saved_code.strip() == ver_code.strip():
            await session.execute(
                UserModel.__table__.update().where(UserModel.verified_code == ver_code).values(is_verified=True)
            )
            await session.commit()
        else:
            raise HTTPException(status_code=404, detail="Verification code is incorrect")
