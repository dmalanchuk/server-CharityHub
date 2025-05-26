from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str


class GetCategories(CategoryBase):
    id: int

    class Config:
        from_attributes = True
