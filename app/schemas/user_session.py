from datetime import datetime, Date
from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr, validator

# Shared properties
class UserSessionBase(BaseModel):
    user_uuid: UUID4 = None
    church_uuid: UUID4 | None= None
    token: str | None = None
    firebase_token: str = False
    

# Properties to receive via API on creation
class UserSessionCreate(UserSessionBase):
    pass

    
class UserInDB(UserSessionBase):
    uuid: UUID4
    created_at: datetime = False
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class UserSession(UserInDB):
    pass
