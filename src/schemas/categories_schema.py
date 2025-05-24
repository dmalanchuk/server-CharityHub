from pydantic import BaseModel


class Category(BaseModel):
    name: str


class GetCategories(BaseModel):
    id: int
    name: str
