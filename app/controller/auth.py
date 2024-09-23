
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import BackgroundTasks, HTTPException
from app.core.security import hash_password, verify_password


from app.core.firebase_config import firebase
from app.models import ChurchUsers
from app.models.User import User
from app.models.UserSessions import UserSession
from app.schemas.church_user import ChurchUserInDB
from app.schemas.user import UserCreate, UserUpdate
from app.services.base import CRUDBase
from app.controller.user_session import user_session as user_session_controller
from app.services.jwt import _generate_tokens
from app.services.email import send_password_reset_email
from app.schemas.auth_schemas import PasswordReset


class AuthController(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db:Session, *, email: str):
        return db.query(self.model).filter(User.email == email).first()
    
    async def post_login_token(self,db:Session, obj_in: OAuth2PasswordRequestForm):
        try:
       
            auth = firebase.auth()
            user = await self.get_by_email(db=db, email=obj_in.username)
            
            if not user:
                raise ValueError("El correo electronico no está registrado con nosotros")
           
            if not verify_password(obj_in.password, user.password):
                raise ValueError("Contraseña invalida o correo electronico")
            
            user_data = auth.sign_in_with_email_and_password(obj_in.username, obj_in.password)
            response = _generate_tokens(user)
            
            church_user = db.query(ChurchUsers).filter(ChurchUsers.user_uuid == user.uuid).first()
            if church_user:
                db_obj_in = {
                    "user_uuid": church_user.user_uuid,
                    "church_uuid": church_user.church_uuid,
                    "token": response.get("access_token"),
                    "firebase_token": user_data['idToken']
                }
                await user_session_controller.create_user_session(session=db, obj_in=db_obj_in)
            return response
        except Exception as ex:
            if "user not found" in str(ex).lower():
                raise HTTPException(status_code=404, detail="Usuario no encontrado en Firebase.")
            elif "invalid password" in str(ex).lower():
                raise HTTPException(status_code=401, detail="Contraseña inválida.")
            else:
                raise HTTPException(status_code=500, detail=f"Error en el inicio de sesión: {str(ex)}")
   
    async def post_logout_user(self, db: Session, church_user: ChurchUserInDB):
        try:
            data_session = db.query(UserSession).filter(UserSession.deleted_at == None, UserSession.church_uuid == church_user.church_uuid, UserSession.user_uuid == church_user.user_uuid).first()
            if data_session:
                user_session_controller.remove_user_session(session=Session, uuid=data_session.uuid)
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(ex)}")
        

    async def forgot_password(self, email: str, db: Session, background_tasks: BackgroundTasks):
        try:
            user = db.query(User).filter(User.email == email).where(User.deleted_at == None).first()
            if not user:
                return None

            await send_password_reset_email(user=user, background_tasks=background_tasks)
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(ex)}")

    async def reset_password(self, obj_in: PasswordReset, db: Session):
        try:
            user = await self.get_by_email(db=db, email=obj_in.email)
            if not user:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            user_token = user.get_context_string(context="PASSWORD-TEST")
            token_valid = verify_password(user_token, obj_in.token)
            if not token_valid:
                raise HTTPException(status_code=400, detail="Token invalido, ya ha expirado")
            
            
            data_user = {"password": hash_password(obj_in.password)}
            self.update(db=db, db_obj=user, obj_in=data_user)

            return {"message": "La contraseña ya ha sido cambiada."}

        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"There is an error: {str(ex)}")
    
        
auth = AuthController(User)
