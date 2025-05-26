from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class CategoriesModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column()
