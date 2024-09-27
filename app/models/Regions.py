
from uuid import uuid4
from sqlalchemy import Column, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel

class Regions(BaseModel):
    __tablename__= 'regions'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )
    
    country_uuid = Column(UUID(200), ForeignKey('countries.uuid'))

    name = Column(String(125))
    
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
    
    # RELACIONES
    
    cities = relationship("Cities", back_populates="regions")
    countries = relationship("Countries", back_populates="regions", uselist=False)