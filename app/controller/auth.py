from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from app.core.security import verify_password

from app.models import ChurchUsers
from app.models.User import User
from app.models.UserSessions import UserSession
from app.schemas.church_user import ChurchUserInDB
from app.schemas.user import UserCreate, UserUpdate
from app.services.base import CRUDBase
from app.controller.user_session import user_session as user_session_controller
from app.services.jwt import _generate_tokens


class AuthController(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db:Session, *, email: str):
        return db.query(self.model).filter(User.email == email).first()
    
    async def post_login_token(self, db:Session, obj_in: OAuth2PasswordRequestForm):
        try:
            user = await self.get_by_email(db=db, email=obj_in.username)
            
            if not user:
                raise ValueError("El correo electronico no está registrado con nosotros")
            if not verify_password(obj_in.password, user.password):
                raise ValueError("Contraseña invalida o correo electronico")
            
            response = _generate_tokens(user)
                
            # INSERTAR SESSION CON ACCESS TOKEN
            church_user = db.query(ChurchUsers).filter(ChurchUsers.user_uuid == user.uuid).first()
            if church_user:
                db_obj_in = {
                    "user_uuid": church_user.user_uuid,
                    "church_uuid": church_user.church_uuid,
                    "token": response.get("access_token"),
                    "firebase_token": None
                }
                await user_session_controller.create_user_session(session=db, obj_in=db_obj_in)
            return response
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(ex)}")
   
    async def post_logout_user(self, db: Session, church_user: ChurchUserInDB):
        try:
            data_session = db.query(UserSession).filter(UserSession.deleted_at == None, UserSession.church_uuid == church_user.church_uuid, UserSession.user_uuid == church_user.user_uuid).first()
            if data_session:
                user_session_controller.remove_user_session(session=Session, uuid=data_session.uuid)
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(ex)}")


auth = AuthController(User)
