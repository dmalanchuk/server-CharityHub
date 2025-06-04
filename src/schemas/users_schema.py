from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    username: str
    email: EmailStr


class GetInfoUser(User):
    id: int
    is_verified: bool

    class Config:
        orm_mode = True


class CreateUser(User):
    password: str = Field(min_length=8)
