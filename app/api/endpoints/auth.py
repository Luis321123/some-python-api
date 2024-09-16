from fastapi import APIRouter, Depends, status, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.api.deps import get_current_church_user
from app.core.database import get_session
from app.controller.auth import auth as auth_controller
from app.models.User import User

router=APIRouter()

@router.post('/login', status_code=status.HTTP_200_OK)
async def user_login(data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    data_in = await auth_controller.post_login_token(db=session, obj_in=data)
    return JSONResponse(data_in)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/logout", status_code=status.HTTP_200_OK)
async def user_logout(session: Session = Depends(get_session), user: User = Depends(get_current_church_user)):
   await auth_controller.post_logout_user(db=session, )
   return JSONResponse(content='pepe')

#@router.post('/refresh', status_code=status.HTTP_200_OK, response_model=LoginResponse)
#async def refresh_token(refresh_token = Header(), session: Session = Depends(get_session)):
   # return await get_refresh_token(refresh_token, session)