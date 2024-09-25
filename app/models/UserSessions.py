from uuid import uuid4
from sqlalchemy import Column, DateTime, String, Text, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel

class UserSession(BaseModel):
    __tablename__ = 'user_session'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    user_uuid =Column(UUID(200), ForeignKey('users.uuid'))
    church_uuid = Column(UUID(200), ForeignKey('churches.uuid'))
   
    token = Column(String(500), unique=True)
    firebase_token = Column(Text)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    #RELEACIONES
    user = relationship("User", back_populates="user_session", uselist=False)
    churches = relationship("Churches", back_populates="user_session", uselist=False)