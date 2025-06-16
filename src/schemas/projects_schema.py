import datetime

from pydantic import BaseModel


class CreateProject(BaseModel):
    title: str
    description: str
    category_id: int
    owner: str
    goal_amount: int
    url_donations: str
    end_date: datetime.datetime
