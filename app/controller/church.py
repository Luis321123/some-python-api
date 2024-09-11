from typing import Optional
from sqlalchemy import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from app.core.security import verify_password



from app.models.Churches import Churches
from app.schemas.user import User as UserSchema
from app.schemas.church import ChurchCreate, ChurchUpdate
from app.services.base import CRUDBase
from app.services.jwt import _generate_tokens

class ChurchController(CRUDBase[Churches, ChurchCreate, ChurchUpdate]):
    async def get_church(self, db:Session):
        pass



church=ChurchController(Churches)
    





