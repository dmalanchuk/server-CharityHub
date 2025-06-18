import datetime

from pydantic import BaseModel


class CreateProject(BaseModel):
    title: str
    description: str
    goal_amount: int
    iban_details: str
    end_date: datetime.datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime('%d.%m.%Y')
        }
