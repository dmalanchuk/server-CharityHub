import datetime

from pydantic import BaseModel


class DonationsBase(BaseModel):
    amount: int
    message: str | None
    donated_at: datetime


class GetDonations(DonationsBase):
    id: int
    user_id: int
    category_id: int
