from typing import Optional
from sqlalchemy import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from app.core.security import verify_password
from schemas.church_user import ChurchUserCreate
from pydantic import UUID4


from app.models.User import User
from app.schemas.user import UserCreate, UserUpdate, UserInDB
from app.services.base import CRUDBase
from app.services.role import role as role_services
from app.controller.church_user import church_user as church_user_controller
from app.schemas.church_user import ChurchUser

class UserController(CRUDBase[User, UserCreate, UserUpdate]):
    async def create_user(self, church_id: str, data: UserCreate, session: Session):
        try:
            user: UserInDB = await self.create(db=session, obj_in=data)
            role = await role_services.get_by_name(db=session, name="member")
            obj_in_church_user = ChurchUserCreate(
                user_uuid=user.uuid,
                church_uuid=church_id, 
                role_uuid=role.uuid, 
                position="test",
                active=True
            )
            await church_user_controller.create_church_user(db=session, obj_in=obj_in_church_user)

            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

user = UserController(User)