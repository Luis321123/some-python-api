from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.Base import BaseModel


class Cities(BaseModel):
    __tablename__= 'cities'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    region_uuid = Column(UUID(150), ForeignKey('regions.id'), index=True)
   
    name = Column(String(120))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)