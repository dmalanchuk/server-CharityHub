# from sqlalchemy.orm import Mapped, mapped_column
# from src.database import Base
#
#
# class UserModel(Base):
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column("id", primary_key=True)
#     name: Mapped[str] = mapped_column("name", nullable=False)
#     email: Mapped[str] = mapped_column("email", nullable=False)
#     email_code: Mapped[int] = mapped_column("email_code", nullable=False)
