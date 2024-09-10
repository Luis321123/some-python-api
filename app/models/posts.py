from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, Longtext
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Posts(Base):
    __tablename__ = 'posts'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    church_uuid = Column(UUID(200))
    title = Column(String(150))
    content = Column(Longtext(200))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)