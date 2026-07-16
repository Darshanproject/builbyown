import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # tasks = relationship("Task", back_populates="user")
    tasks = relationship(
    "Task",
    foreign_keys="Task.user_id",
    back_populates="user"
)
    categories = relationship("Category", back_populates="user")
    profile_image: Mapped[str | None] = mapped_column(
    String(500),
    nullable=True
)
    is_verified = mapped_column(
    Boolean,
    default=False
)
    role: Mapped[str] = mapped_column(
    String(20),
    default="user"
)

is_active: Mapped[bool] = mapped_column(
    Boolean,
    default=True
)

is_banned: Mapped[bool] = mapped_column(
    Boolean,
    default=False
)