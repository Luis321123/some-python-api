
from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.models.BaseModel import BaseModel

class Regions(BaseModel):
    __tablename__= 'regions'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )


    name = Column(String(125))
    
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)