from pydantic import BaseModel


class CreateProject(BaseModel):
    title: str
    description: str
    category: str
    goal_amount: int
    url_donations: str
