from datetime import date

from pydantic import BaseModel


class CreateProject(BaseModel):
    title: str
    description: str
    category: str
    goal_amount: int
    iban_details: str
    end_date: date

    class Config:
        json_encoders = {
            date: lambda v: v.strftime('%d.%m.%Y')
        }
