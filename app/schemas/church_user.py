from datetime import datetime, Date
from typing import Optional
from pydantic import UUID4, BaseModel
# Shared properties
class ChurchUser(BaseModel):
    user_uuid: UUID4 = None
    church_uuid: UUID4 | None= None
    role_uuid: UUID4 | None = None
    position: str = None
    active: bool = False
    

# Properties to receive via API on creation
class ChurchUserCreate(ChurchUser):
   pass


class ChurchUserUpdate(ChurchUser):
    pass

    
class ChurchUserInDB(ChurchUser):
    uuid: UUID4
    created_at: datetime = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class ChurchUserSession(ChurchUserInDB):
    pass
