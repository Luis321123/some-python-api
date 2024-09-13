from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.church import ChurchCreate, ChurchUpdate, ChurchInD, ChurchBase
from app.models.Churches import Churches, uuid
from app.controller.church import church as church_controller
from app.api.deps import get_current_user, get_current_admin, get_current_is_superuser

router = APIRouter()

@router.get('/me/{id}',status_code=status.HTTP_200_OK)
async def get_church(id: str, session: Session = Depends(get_session)):
    church_current = await church_controller.get_church(db=Session, id=id)
    return church_current

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_church(data:ChurchCreate, session: Session = Depends(get_session), user: User = Depends(get_current_is_superuser)):
    church_create = await church_controller.create_church(db=session, obj_in=data)
    return JSONResponse({'message': 'created'})

@router.put('update/{id}', status_code=status.HTTP_200_OK)
async def update_church(id: str, data:ChurchUpdate, session: Session = Depends(get_session)):
    await church_controller.update_church(data=data, church_id=id, session=session)
    return JSONResponse({'message': 'updated'})

@router.delete('/delete/{id}',status_code=status.HTTP_200_OK)
async def delete_church(id: str, session: Session = Depends(get_session)):
    await church_controller.delete_church(church_id=id, session=session)
    return JSONResponse({'message': 'Deleted'})
