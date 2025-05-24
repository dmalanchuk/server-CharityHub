import datetime

from pydantic import BaseModel


class GetDonations(BaseModel):
    id: int
    user_id: int
    product_id: int
    amount: int
    message: str
    donated_at: datetime


class Donations(BaseModel):
    amount: int
    message: str
    donated_at: datetime
