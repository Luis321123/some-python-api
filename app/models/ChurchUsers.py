from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel


class ChurchUsers(BaseModel):
    __tablename__ = 'church_users'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )

    church_uuid = Column(UUID(200), ForeignKey('churches.uuid'))
    user_uuid = Column(UUID(200), ForeignKey('users.uuid'))
    role_uuid = Column(UUID(200), ForeignKey('roles.uuid'))

    position = Column(String(150), index=True)
    active = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
    
    #RELACIONES
    
    user = relationship("User", back_populates="church_user", uselist=False)
    church = relationship("Churches", back_populates="church_user", uselist= False)
    roles = relationship ( "Roles", back_populates="church_users", uselist= False)