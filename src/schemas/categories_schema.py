from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class GetCategories(CategoryBase):
    id: int

