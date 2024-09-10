from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Churches(Base):
    __tablename__ = 'churches'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    church_denomination_uuid = Column(UUID(200))
    name = Column(String(150))
    fullname = Column(String(50), unique=True, index=True)
    city_uuid = Column(UUID(150), index=True)
    active = Column(Boolean[True])
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)