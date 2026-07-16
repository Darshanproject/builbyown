from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.models.base import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    color = Column(
        String,
        default="#2196F3"
    )

    tasks = relationship(
        "Task",
        secondary="task_tags",
        back_populates="tags"
    )