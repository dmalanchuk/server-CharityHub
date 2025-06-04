from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.users_model import UserModel
from schemas.users_schema import CreateUser


class RegistrationUser:

    @classmethod
    async def get_by_email(cls, email: str, session: AsyncSession):
        result = await session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalars().first()

    @classmethod
    async def reg_user_by_email(cls, data: dict, session: AsyncSession):
        new_user = CreateUser(**data)

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user
