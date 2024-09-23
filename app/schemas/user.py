from datetime import datetime, date
from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr
from sqlalchemy import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class UserBase(BaseModel):
    name: str = None
    last_name: str = None
    is_superuser: bool = False
    email: EmailStr = None
    birth: date | None = None
    phone: str = None
    address: str = None
    city_uuid: Optional[UUID4] = None   
    country_uuid: Optional[UUID4] = None   
    avatar: Optional[UUID4] = None   
    gender: str = None # VALIDATE FOR GENDER ENUM


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    uuid: UUID4
    created_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class User(UserInDB):
    pass
