from datetime import datetime
import uuid

from sqlalchemy import Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    title: Mapped[str] = mapped_column(Text)

    message: Mapped[str] = mapped_column(Text)

    is_read: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    created_at = mapped_column(
        DateTime,
        default=datetime.utcnow
    )