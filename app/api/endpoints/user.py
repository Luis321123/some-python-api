from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.controller.user import user as user_controller
from app.schemas.user import UserCreate

router= APIRouter()

@router.post('/create/{id}', status_code=status.HTTP_201_CREATED)
async def user_create(church_uuid: str, data:UserCreate, session: Session = Depends(get_session)):
    await user_controller.create_user(church_id=church_uuid, data=data, session=session)
    return JSONResponse({'message': 'created'})

