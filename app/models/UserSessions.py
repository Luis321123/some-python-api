from datetime import datetime
from uuid import uuid4
from sqlalchemy import Boolean, Column, DateTime, String, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base

class UserSession(Base):
    __tablename__ = 'user_session'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    user_uuid =Column(UUID(200))
    church_uuid = Column(UUID(200))
    token = Column(String(255), unique=True)
    firebase_token = Column(String(250))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)