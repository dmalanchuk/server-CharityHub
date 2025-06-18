import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class ProjectsModel(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    goal_amount: Mapped[int] = mapped_column(nullable=False)
    current_amount: Mapped[int] = mapped_column(nullable=False, default=0)
    start_date: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)
    end_date: Mapped[datetime.datetime] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    iban_details: Mapped[str] = mapped_column(nullable=False)
