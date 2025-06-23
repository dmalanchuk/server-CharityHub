import random

from fastapi import HTTPException
from pydantic import EmailStr

from src.core.email_utils import send_verification_code_sync
from src.core.security_pw import hash_password

from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.users_schema import CreateUser
from src.repositories.auth.registration_repo import RegistrationUser



class RegistrationService:

    @staticmethod
    async def auth_registration_user_service(data: CreateUser, session: AsyncSession):
        existing_user = await RegistrationUser.get_by_email(data.email, session)
        if existing_user:
            raise HTTPException(status_code=409, detail="Email is already registered")

        new_user_data = {
            "username": data.username,
            "email": data.email,
            "password": hash_password(data.password),
            "is_verified": False,
            "verified_code": None,
        }

        return await RegistrationUser.reg_user_by_email(new_user_data, session)

    @staticmethod
    async def get_verification_code(email: EmailStr, session: AsyncSession):
        get_user = await RegistrationUser.get_by_email(email, session)

        if not get_user:
            raise HTTPException(status_code=404, detail="User not found")

        verification_code = str(random.randint(100000, 999999))

        await RegistrationUser.save_verification_code(get_user, verification_code, session)

        send_verification_code_sync(verification_code, email)
        return {"msg": "Verification code has been sent"}
