from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    username: str
    email: EmailStr


class LoginUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class GetVerifyUser(User):
    is_verified: bool

    class Config:
        from_attributes = True


class CreateUser(User):
    password: str = Field(min_length=8)
