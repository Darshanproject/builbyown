from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base


class TaskTag(Base):
    __tablename__ = "task_tags"

    task_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id"),
        primary_key=True
    )

    tag_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tags.id"),
        primary_key=True
    )