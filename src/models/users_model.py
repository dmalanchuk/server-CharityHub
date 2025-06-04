from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False ,nullable=False)
    verified_code: Mapped[str] = mapped_column()
