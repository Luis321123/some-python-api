from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel

# Shared properties
class ChurchBase(BaseModel):
    name: str  | None= None
    fullname: str = None
    phone: str = None
    address: str = None
    city_uuid: Optional[UUID4] = None    
    active: bool = False 

# Properties to receive via API on creation
class ChurchCreate(ChurchBase):
    pass

class ChurchUpdate(ChurchBase):
    pass

class ChurchInDB(ChurchBase):
    uuid: UUID4
    created_at: datetime = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class Church(ChurchInDB):
    pass