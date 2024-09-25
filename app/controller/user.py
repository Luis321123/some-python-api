from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.core.firebase_config import firebase
from app.core.security import hash_password, is_password_strong_enough
from app.schemas.church_user import ChurchUserCreate
from app.models.User import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.base import CRUDBase
from app.services.role import role as role_services
from app.controller.church_user import church_user as church_user_controller

class UserController(CRUDBase[User, UserCreate, UserUpdate]):
    async def create_user(self, church_id: str, data: UserCreate, session: Session):
        try:
            print(data.password)
            if not is_password_strong_enough(data.password):
                raise HTTPException(status_code=400, detail="Please provide a strong password.")
            auth = firebase.auth()
            auth.create_user_with_email_and_password(data.email, data.password)
            data.password = hash_password(data.password)
            data.is_superuser = False
            user = self.create(db=session, obj_in=data)
            role = role_services.get_by_name(db=session, name="member")
            obj_in_church_user = ChurchUserCreate(
                user_uuid=user.uuid,
                church_uuid=church_id, 
                role_uuid=role.uuid, 
                position="test",
                active=True
            )
            await church_user_controller.create_church_user(session=session, data=obj_in_church_user)

            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

user = UserController(User)