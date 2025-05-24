from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr


class GetUser(BaseModel):
    id: int
    name: str
    email: EmailStr
