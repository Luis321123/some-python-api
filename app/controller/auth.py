
from typing import Optional
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from app.core.security import verify_password

from app.models.User import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.base import CRUDBase
from app.services.jwt import _generate_tokens

class AuthController(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db:Session, *, email: str):
        return db.query(self.model).filter(User.email == email).first()
    
    async def post_login_token(self, db:Session, obj_in: OAuth2PasswordRequestForm):
        try:
            user = self.get_by_email(db=db, email=obj_in.username)
            
            if not user:
                raise ValueError("El correo electronico no está registrado con nosotros")
            if not verify_password(obj_in.password, user.password):
                raise ValueError("Contraseña invalida o correo electronico")
            
            response = _generate_tokens(user)
            return response
      
      
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(ex)}")

auth = AuthController(User)
