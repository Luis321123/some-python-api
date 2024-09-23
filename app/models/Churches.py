from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.BaseModel import BaseModel


class Churches(BaseModel):
    __tablename__ = 'churches'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    church_denomination_uuid = Column(UUID(200), ForeignKey('church_denominations.uuid'))
    name = Column(String(150))
    fullname = Column(String(200), unique=True, index=True)
    city_uuid = Column(UUID(150), index=True)
    active = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    #RELEACIONES

    church_user = relationship("ChurchUsers", back_populates= "church")
    church_denomination = relationship("ChurchDenominations", back_populates= "church", uselist=False)
    post = relationship("Posts", back_populates= "church")
