from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.Base import BaseModel


class ChurchUsers(BaseModel):
    __tablename__ = 'church_user'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    church_uuid = Column(UUID(200))
    user_uuid = Column(UUID(200))
    role_uuid = Column(UUID(200), index=True)
    position = Column(String(150), index=True)
    active = Column(Boolean[True])
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)