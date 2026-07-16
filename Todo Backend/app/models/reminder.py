# import uuid
# from datetime import datetime

# from sqlalchemy import DateTime, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy.dialects.postgresql import UUID

# from app.models.base import Base


# class Reminder(Base):
#     __tablename__ = "reminders"

#     id: Mapped[uuid.UUID] = mapped_column(
#         UUID(as_uuid=True),
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     task_id: Mapped[uuid.UUID] = mapped_column(
#         ForeignKey("tasks.id")
#     )

#     remind_at: Mapped[datetime] = mapped_column(
#         DateTime
#     )

from uuid import uuid4
from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    Boolean,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Reminder(Base):
    __tablename__ = "reminders"

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

    reminder_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),nullable=False
    )

    recurring_type: Mapped[str] = mapped_column(
        String(20),
        default="once"
    )
    # once
    # daily
    # weekly
    # monthly

    is_completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )