from uuid import uuid4
from datetime import datetime

from sqlalchemy import String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    content: Mapped[str] = mapped_column(
        Text
    )

    is_pinned: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_archived: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_favorite: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    attachment_url: Mapped[str | None] = mapped_column(
    String(500),
    nullable=True
)