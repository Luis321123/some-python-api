from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session, joinedload

from app.core.database import get_session
from app.services.jwt import get_token_user
from app.models.User import User
from app.models import ChurchUsers

message_not_authorised = 'Not authorised, consult an administrator'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(request: Request, optional_token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    token = request.cookies.get('access_token')
    if token:
        user = await get_token_user(token=token, db=db)
    elif optional_token:
        user = await get_token_user(token=optional_token, db=db)
    if user: 
        return user
    raise HTTPException(status_code=401, detail=message_not_authorised)

async def get_current_admin(request: Request, optional_token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    user = await get_current_user(request=request, optional_token=optional_token, db=db)

    church_user_with_role = (
            db.query(ChurchUsers)
            .options(joinedload(ChurchUsers.roles))
            .filter(ChurchUsers.user_uuid == user.uuid)
            .first()
    )
    role_name = church_user_with_role.roles.name

    if role_name != 'administrador': 
        raise HTTPException(status_code=401, detail=message_not_authorised)
    return user


async def get_current_is_superuser(request: Request, optional_token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    user = await get_current_user(request=request, optional_token=optional_token, db=db)
    
    if not user.is_superuser:
        raise HTTPException(status_code=401, detail=message_not_authorised)
    return user