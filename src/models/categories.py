from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from src.database import Base


class UserModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    name: Mapped[str]
