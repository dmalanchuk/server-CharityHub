from sqlalchemy.future import select

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.models.users_model import UserModel

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

async def get_current_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login/email")),
    session: AsyncSession = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    query = select(UserModel).where(UserModel.email == user_email)
    result = await session.execute(query)
    user = result.scalars().first()

    if user is None:
        raise credentials_exception
    return user
