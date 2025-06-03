from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class GetInfoUser(User):
    id: int
    is_verified: bool


class CreateUser(User):
    password: str
    verified_code: str
