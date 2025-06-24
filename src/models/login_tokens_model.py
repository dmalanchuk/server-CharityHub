import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class LoginTokens(Base):
    __tablename__ = "login_tokens"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    refresh_token: Mapped[str] = mapped_column(nullable=False)
    revoked: Mapped[bool] = mapped_column(nullable=False)
    expires_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(nullable=False)

    user = relationship("UserModel", back_populates="tokens")
