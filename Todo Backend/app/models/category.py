import uuid

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    color: Mapped[str] = mapped_column(
        String(20),
        default="#2196F3"
    )

    user = relationship("User", back_populates="categories")

    tasks = relationship(
        "Task",
        back_populates="category"
    )