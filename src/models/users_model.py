from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
