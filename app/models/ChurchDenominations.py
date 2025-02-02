from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel


class ChurchDenominations(BaseModel):
    __tablename__ = 'church_denominations'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )
   
    name = Column(String(150))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    # RELACIONES

    church = relationship("Churches", back_populates= "church_denomination")
