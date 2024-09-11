from typing import Optional
from sqlalchemy import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from app.core.security import verify_password



from app.models.User import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.base import CRUDBase


class UserController(CRUDBase[User, UserCreate, UserUpdate]):
    async def create_user(self, id: str, data: UserCreate, session: Session):
        try:
            user = await self.create(db=session, obj_in=data)
            return user
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

            



     
    


user = UserController(User)