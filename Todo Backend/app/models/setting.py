import uuid

from sqlalchemy import Boolean, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


class Settings(Base):
    __tablename__ = "settings"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    theme: Mapped[str] = mapped_column(
        String(20),
        default="light"
    )

    notifications: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )