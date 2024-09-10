from uuid import uuid4
from sqlalchemy import Column, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.Base import BaseModel


class PostsFiles(BaseModel):
    __tablename__ = 'posts_files'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )
  
    post_uuid = Column(UUID(200), ForeignKey('posts.id'))
    file_uuid = Column(UUID(150), ForeignKey('files.id'))

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)