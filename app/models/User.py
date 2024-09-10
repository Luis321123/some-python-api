
from uuid import uuid4
from sqlalchemy import Column, DateTime, String ,Integer ,  Date, Enum , func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.Base import BaseModel

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class User(BaseModel):
    __tablename__ = 'users'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4

    )

    city_uuid = Column(UUID(150), ForeignKey('cities.id'), index=True)
    country_uuid = Column(UUID(150), ForeignKey('countries.id'), default=None)

    avatar = Column(UUID(150), nullable=True, default=None)
    name = Column(String(50))
    last_name = Column(String(150))
    email = Column(String(50), unique=True, index=True)
    birth = Column(Date)
    phone = Column(String(20), index=True)
    address = Column(String(125), index=True)
    gender = Column(Enum(Gender), nullable=False, default=None)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    def get_context_string(self, context: str):
        return f"{context}{self.password[-6:]}{self.create_at.strftime('%m%d%Y%H%M%S')}".strip()
    


    user_session = relationship("UserSession", back_populates="user", uselist=False)
    files = relationship("Files", back_populates="user")
    countries = relationship("Countries", back_populates="user", uselist=False)
    cities = relationship("Cities", back_populates="user", uselist=False)
    role = relationship("Roles", back_populates="user", uselist=False)
    churches = relationship("Churches", back_populates="user", uselist=False)