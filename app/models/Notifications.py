from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel


class Notifications(BaseModel):
    __tablename__ = 'notifications'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    user_uuid = Column(UUID(200), ('users.uuid'))
    church_uuid = Column(UUID(200), ForeignKey ('churches.uuid'))
    titulo = Column(Text(100))
    description = Column(String(150))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
