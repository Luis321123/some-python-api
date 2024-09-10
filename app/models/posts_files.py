from uuid import uuid4
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Posts_files(Base):
    __tablename__ = 'posts_files'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    post_uuid = Column(UUID(200))
    file_uuid = Column(UUID(150))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)