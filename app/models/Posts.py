from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel


class Posts(BaseModel):
    __tablename__ = 'posts'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )
    
    church_uuid = Column(UUID(200), ForeignKey('churches.uuid'))

    title = Column(String(150))
    content = Column(Text)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    # RELACIONES
    
    post_files = relationship("PostsFiles", back_populates="post")
    church = relationship("Churches", back_populates= "post")
