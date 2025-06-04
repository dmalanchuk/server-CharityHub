import random

from fastapi import HTTPException

from src.core.email_utils import send_verification_code
from src.core.security_pw import hash_password

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.users_schema import CreateUser
from src.repositories.auth.registration_repo import RegistrationUser



class RegistrationService:

    @staticmethod
    async def auth_registration_user_service(data: CreateUser, session: AsyncSession):
        existing_user = await RegistrationUser.get_by_email(data.email, session)
        if existing_user:
            raise ValueError("User with this email already exists")


        new_user_data = {
            "username": data.username,
            "email": data.email,
            "password": hash_password(data.password),
            "is_verified": False,
            "verification_code": None
        }

        return await RegistrationUser.reg_user_by_email(new_user_data, session)

    @staticmethod
    async def get_verification_code(email: str, session: AsyncSession):
        get_user = await RegistrationUser.get_by_email(email, session)

        if not get_user:
            raise HTTPException(status_code=404, detail="User not found")

        verification_code = str(random.randint(100000, 999999))
        get_user.verification_code = verification_code

        await send_verification_code(email, verification_code)
        return {"msg": "Verification code has been sent"}
