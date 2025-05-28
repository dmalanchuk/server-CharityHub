from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr


class GetUser(User):
    id: int


class UserCreate(User):
    email_code: int
