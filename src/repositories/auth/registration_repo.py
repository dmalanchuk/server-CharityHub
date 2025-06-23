from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users_model import UserModel
from src.schemas.users_schema import CreateUser


class RegistrationUser:

    @classmethod
    async def get_by_email(cls, email: EmailStr, session: AsyncSession):
        result = await session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalars().first()

    @classmethod
    async def reg_user_by_email(cls, data: CreateUser, session: AsyncSession):
        new_user = UserModel(**data)

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user

    @classmethod
    async def save_verification_code(cls, user: UserModel, verification_code: str, session: AsyncSession):
        user.verification_code = verification_code
        await session.execute(
            UserModel.__table__.update().where(UserModel.id == user.id).values(verified_code=verification_code)
        )
        await session.commit()

