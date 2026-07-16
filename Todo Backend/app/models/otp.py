import datetime
import uuid

from sqlalchemy import String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.models.base import Base

class OTP(Base):
    __tablename__ = "otp_codes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    code: Mapped[str] = mapped_column(
        String(6)
    )

    purpose: Mapped[str] = mapped_column(
        String(50)
    )

    is_used: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    expires_at: Mapped[DateTime] = mapped_column(
    DateTime,
    default=datetime.utcnow
)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )