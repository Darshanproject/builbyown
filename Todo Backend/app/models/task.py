import uuid
from datetime import datetime, date, time

from sqlalchemy import (
    String,
    Text,
    Boolean,
    Date,
    Time,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base



class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("categories.id"),
        nullable=True
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        default="medium"
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_important: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    due_date: Mapped[date] = mapped_column(
        Date,
        nullable=True
    )

    due_time: Mapped[time] = mapped_column(
        Time,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
    "User",
    foreign_keys=[user_id],
    back_populates="tasks"
)

    category = relationship(
        "Category",
        back_populates="tasks"
    )

    # attachment_url = mapped_column(
    # String,
    # nullable=True
    # )

    is_recurring = mapped_column(
    Boolean,
    default=False
    )

    recurring_type = mapped_column(
    String,
    nullable=True
    )

    tags = relationship(
    "Tag",
    secondary="task_tags",
    back_populates="tasks"
)
    attachment_url: Mapped[str | None] = mapped_column(
    String(500),
    nullable=True
)
    assigned_to = mapped_column(
    ForeignKey("users.id"),
    nullable=True
)

assigned_by = mapped_column(
    ForeignKey("users.id"),
    nullable=True
)
recurring_generated = mapped_column(
    Boolean,
    default=False
)