from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr


class GetInfoUser(User):
    id: int
    is_verified: bool


class CreateUser(User):
    password: str
