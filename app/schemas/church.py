from datetime import datetime, Date
from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr, validator, default


# Shared properties
class ChurchBase(BaseModel):
    name: str  | None= None
    fullname: str = None
    active: Date | None = None
    phone: str = False
    address: str = False
    city_uuid: UUID4[str] = None    
    active: bool [default: False]  

# Properties to receive via API on creation
class ChurchCreate(ChurchBase):
    password: str

class ChurchUpdate(ChurchBase):
    pass

class ChurchInDB(ChurchBase):
    uuid: UUID4
    created_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class User(ChurchInDB):
    pass