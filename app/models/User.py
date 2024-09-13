
from uuid import uuid4
from sqlalchemy import Column, DateTime, String , Boolean ,  Date, Enum , func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.BaseModel import BaseModel

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class User(BaseModel):
    __tablename__ = 'users'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4

    )

    city_uuid = Column(UUID(150), ForeignKey('cities.uuid'), nullable=True, index=True)
    country_uuid = Column(UUID(150), ForeignKey('countries.uuid'), nullable=True, default=None)

    avatar = Column(UUID(150), nullable=True, default=None)
    name = Column(String(150))
    last_name = Column(String(150))
    is_superuser=Column(Boolean, default=False)
    email = Column(String(255), unique=True, index=True)
    birth = Column(Date, nullable=True)
    phone = Column(String(20), index=True)
    address = Column(String(125), index=True)
    gender = Column(String(12))
    password = Column(String(100))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    def get_context_string(self, context: str):
        return f"{context}{self.password[-6:]}{self.create_at.strftime('%m%d%Y%H%M%S')}".strip()
    
    #RELEACIONES

    files = relationship("Files", back_populates="user")
    church_user = relationship("ChurchUsers", back_populates="user")
    user_session = relationship("UserSession", back_populates="user", uselist=False)
    countries = relationship("Countries", back_populates="user", uselist=False)
    cities = relationship("Cities", back_populates="user", uselist=False)