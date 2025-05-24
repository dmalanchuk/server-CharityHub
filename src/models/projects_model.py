import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from src.database import Base


class UserModel(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    goal_amount: Mapped[int]
    current_amount: Mapped[int]
    category_id: Mapped[int] = mapped_column("category_id", primary_key=True)
    owner_id: Mapped[int] = mapped_column("user_id", primary_key=True)
    start_date: Mapped[datetime] = mapped_column("start_date", primary_key=True)
    end_date: Mapped[datetime] = mapped_column("end_date", primary_key=True)
