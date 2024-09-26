
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter
from app.schemas.ProviderAuth import ProviderAuth
from google.auth.transport import requests
from google.oauth2 import id_token

from app.core.firebase_config import auth
from app.api.deps import get_current_church_user
from app.core.database import get_session
from app.controller.auth import auth as auth_controller


from app.schemas.auth_schemas import PasswordResetRequest, PasswordReset
from app.schemas.church_user import ChurchUserInDB

router=APIRouter()

@router.post('/login', status_code=status.HTTP_200_OK)
async def user_login(data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    data_in = await auth_controller.post_login_token(db=session, obj_in=data)
    return JSONResponse(data_in)

@router.put("/logout", status_code=status.HTTP_200_OK)
async def user_logout(session: Session = Depends(get_session), church_user: ChurchUserInDB = Depends(get_current_church_user)):
   await auth_controller.post_logout_user(db=session, church_user=church_user)
   return JSONResponse(content='Has cerrado sesion')


@router.post("/forgot-password", status_code=status.HTTP_200_OK)
async def forgot_password(data: PasswordResetRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_session)):
    await auth_controller.forgot_password(email=data.email, db=db, background_tasks=background_tasks)
    return JSONResponse(content='Se ha enviado un correo de verificacion a su gmail')

@router.put("/reset-password", status_code=status.HTTP_200_OK)
async def reset_password(obj_in: PasswordReset, session: Session = Depends(get_session)):
    await auth_controller.reset_password(obj_in=obj_in, db=session)
    return JSONResponse(content='Se ha reiniciado su contraseña')


@router.get('/checkout-google',status_code=status.HTTP_200_OK)
async def get_link_google_auth():
    current_session = await auth_controller.get_link_google_auth()
    return current_session


@router.post("/login/google")
async def login_with_google(data: ProviderAuth):
    try:
        # Crea una instancia de Request
        request_instance = requests.Request()  
        
        # Verifica el token de ID recibido
        decoded_token = id_token.verify_oauth2_token(data.token, request_instance, '129026009710-ru12epb07jd2h3emdpvl3ov3qphohgfl.apps.googleusercontent.com')  # Asegúrate de usar el CLIENT_ID correcto
        uid = decoded_token['sub']  # 'sub' contiene el UID del usuario
        return {"message": "Has iniciado sesión correctamente", "uid": uid}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error al autenticar: {str(ex)}")
   
    except ValueError as ve:
        # Captura errores de valor, como un token inválido
        raise HTTPException(status_code=400, detail=f"Error de valor: {str(ve)}")
    
    except Exception as ex:
        # Captura cualquier otro tipo de excepción
        raise HTTPException(status_code=500, detail=f"Error al autenticar: {str(ex)}")


   