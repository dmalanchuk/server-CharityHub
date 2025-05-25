from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class CategoriesModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    title: Mapped[str]
