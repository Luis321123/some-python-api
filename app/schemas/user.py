from datetime import datetime, Date
from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr, validator


# Shared properties
class UserBase(BaseModel):
    name: str  | None= None
    last_name: str = None
    is_superuser:bool = False
    email: EmailStr | None= None
    birth: Date | None = None
    phone: str = False
    address: str = False
    city_uuid: UUID4[str] = None
    country_uuid: UUID4[str] = None
    avatar: UUID4[str]= None
    gender: str = None


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
