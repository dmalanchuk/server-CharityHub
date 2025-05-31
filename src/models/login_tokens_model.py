# import datetime
#
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column
# from src.database import Base
#
#
#
#
# class LoginTokens(Base):
#     __tablename__ = "login_tokens"
#
#     id: Mapped[int] = mapped_column("id", primary_key=True)
#     user_id: Mapped[str] = mapped_column("user_id", ForeignKey("users.id"))
#     token: Mapped[str] = mapped_column("token", nullable=False)
#     revoked: Mapped[bool] = mapped_column("revoked", nullable=False)
#     created_at: Mapped[datetime.datetime] = mapped_column("created_at", nullable=False)
#     expires_at: Mapped[datetime.datetime] = mapped_column("expires", nullable=False)
