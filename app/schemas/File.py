from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel

 

class FileBase(BaseModel):
    name: str = None
    path: str = None
    ext: str = None
    size: int = None
    folder: str = None
    active: bool = False 


# Properties to receive via API on creation
class FileSave(FileBase):
    user_id: UUID4

class FileUpdate(FileBase):
    pass

class FileInDBBase(FileBase):
    uuid: UUID4
    created_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class User(UserInDB):
    pass
