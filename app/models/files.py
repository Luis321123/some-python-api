from uuid import uuid4
from sqlalchemy import Column, DateTime, String ,Integer,func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base

class Files(Base):
    __tablename__ = 'files'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    name = Column(String(50))
    path = Column(String(150))
    ext = Column(String(50))
    size = Column(Integer)
    folder = Column(String(20))
    user_uuid= Column(200)
    active = Column(String(125), index=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
