"""Database models."""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Patient(Base):
    __tablename__ = "patient"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    date_of_birth: Mapped[str]
