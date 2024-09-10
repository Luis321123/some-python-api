from uuid import uuid4
from sqlalchemy import Column, DateTime, String ,Integer ,  Date, Enum , func
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

    name = Column(String(50))
    last_name = Column(String(150))
    email = Column(String(50), unique=True, index=True)
    birth = Column(Date)
    phone = Column(String(20), index=True)
    address = Column(String(125), index=True)
    city_uuid = Column(UUID(150), index=True)
    country_uuid = Column(UUID(150), default=None)
    avatar = Column(Integer, nullable=True, default=None)
    gender = Column(Enum(Gender), nullable=False, default=None)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    #ADD RELATIONS

    def get_context_string(self, context: str):
        return f"{context}{self.password[-6:]}{self.create_at.strftime('%m%d%Y%H%M%S')}".strip()