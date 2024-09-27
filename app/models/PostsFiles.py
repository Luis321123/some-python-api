from uuid import uuid4
from sqlalchemy import Column, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel


class PostsFiles(BaseModel):
    __tablename__ = 'posts_files'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )
  
    post_uuid = Column(UUID(200), ForeignKey('posts.uuid'))
    file_uuid = Column(UUID(150), ForeignKey('files.uuid'))

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    post = relationship("Posts", back_populates="post_files", uselist=False)
    file = relationship("Files", back_populates="post_file", uselist=False)