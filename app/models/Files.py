from uuid import uuid4
from sqlalchemy import Column, DateTime, String ,Integer,func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.Base import BaseModel

class Files(BaseModel):
    __tablename__ = 'files'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )
    user_uuid= Column((200),ForeignKey('users.id'))

    name = Column(String(50))
    path = Column(String(150))
    ext = Column(String(50))
    size = Column(Integer)
    folder = Column(String(20))
    active = Column(String(125), index=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    user = relationship("User", backpopulates="files")