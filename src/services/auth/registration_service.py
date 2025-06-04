from core.security_pw import hash_password
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.users_schema import CreateUser
from repositories.auth.registration_repo import RegistrationUser

import random


class RegistrationService:

    @staticmethod
    async def auth_registration_user_service(data: CreateUser, session: AsyncSession):
        existing_user = await RegistrationUser.get_by_email(data.email, session)
        if existing_user:
            raise ValueError("User with this email already exists")


        verification_code = str(random.randint(100000, 999999))

        new_user_data = {
            "username": data.username,
            "email": data.email,
            "password": hash_password(data.password),
            "is_verified": False,
            "verification_code": verification_code
        }

        return await RegistrationUser.reg_user_by_email(new_user_data, session)
