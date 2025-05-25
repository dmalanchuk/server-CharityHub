import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class DonationsModel(Base):
    __tablename__ = "donations"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    user_id: Mapped[int] = mapped_column("user_id", ForeignKey("users.id"))
    project_id: Mapped[int] = mapped_column("project_id", ForeignKey("projects.id"))
    amount: Mapped[float] = mapped_column("amount", nullable=False)
    message: Mapped[str] = mapped_column("message", nullable=False)
    donated_at: Mapped[datetime.datetime] = mapped_column("donated_at", nullable=False)
