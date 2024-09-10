from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Cities(Base):
    __tablename__= 'cities'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    region_uuid = Column(UUID(150), index=True)
    name = Column(String(120))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)