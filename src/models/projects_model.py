import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from src.database import Base


class UserModel(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    title: Mapped[str] = mapped_column("title", nullable=False)
    description: Mapped[str] = mapped_column("description", nullable=False)
    goal_amount: Mapped[int] = mapped_column("goal_amount", nullable=False)
    current_amount: Mapped[int] = mapped_column("current_amount", nullable=False)
    category_id: Mapped[int] = mapped_column("category_id", ForeignKey("categories.id"))
    owner_id: Mapped[int] = mapped_column("user_id", ForeignKey("users.id"))
    start_date: Mapped[datetime] = mapped_column("start_date")
    end_date: Mapped[datetime] = mapped_column("end_date")
