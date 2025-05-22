from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from src.database import Base


class UserModel(Base):
    __tablename__ = "donations"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    user_id: Mapped[int] = mapped_column("user_id", primary_key=True)
    project_id: Mapped[int] = mapped_column("project_id", primary_key=True)
    amount: Mapped[float] = mapped_column("amount", nullable=False)
    message: Mapped[str] = mapped_column("message", nullable=False)
    donated_at: Mapped[datetime] = mapped_column("donated_at", nullable=False)
