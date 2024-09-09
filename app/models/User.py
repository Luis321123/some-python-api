from datetime import datetime
from uuid import uuid4
from sqlalchemy import Boolean, Column, DateTime, String, func,Integer,  Date, Enum , Note
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class User(Base):
    __tablename__ = 'users'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(50), unique=True, index=True)
    birth = Column(Date)
    phone = Column(String(20), index=True)
    address = Column(String(125), index=True)
    city_uuid = Column(Integer, index=True)
    country_uuid = Column(Integer, default=None)
    avatar = Column(Integer, nullable=True, default=None)
    gender = Column(Enum(Gender), nullable=False, default=None)
    password = Column(String(50), nullable=False, server_default=None)
    created_at = Column(DateTime, nullable=False, server_default=None)
    deleted_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)

    def get_context_string(self, context: str):
        return f"{context}{self.password[-6:]}{self.create_at.strftime('%m%d%Y%H%M%S')}".strip()