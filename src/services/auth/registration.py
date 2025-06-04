from core.security_pw import hash_password
from sqlalchemy.ext.asyncio import AsyncSession
from models.users_model import UserModel
from sqlalchemy.future import select

import random


async def auth_registration_user_service(username: str, password: str
                                , email: str, session: AsyncSession):
    result = await session.execute(select(UserModel).where(UserModel.email == email))
    if result.scalars().one_or_none():
        raise ValueError("You are not registered")

    verified_code = str(random.randint(100000, 999999))

    new_user = UserModel(
        username=username,
        email=email,
        password=hash_password(password),
        is_verified=False,
        verified_code=verified_code
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user
