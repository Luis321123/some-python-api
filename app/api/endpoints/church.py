from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.church import ChurchCreate, ChurchUpdate
from app.schemas.user import User
from app.controller.church import church as church_controller
from app.api.deps import get_current_is_superuser

router = APIRouter()

@router.get('/me/{church_uuid}',status_code=status.HTTP_200_OK)
async def get_church(church_uuid: str, session: Session = Depends(get_session)):
    church_current = await church_controller.get_church(db=session, id=church_uuid)
    return church_current

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_church(data:ChurchCreate, session: Session = Depends(get_session), user: User = Depends(get_current_is_superuser)):
    await church_controller.create_church(session=session, data=data)
    return JSONResponse({'message': 'created'})

@router.put('/update/{id}', status_code=status.HTTP_200_OK)
async def update_church(id: str, data:ChurchUpdate, session: Session = Depends(get_session)):
    await church_controller.update_church(data=data, church_id=id, session=session)
    return JSONResponse({'message': 'updated'})

@router.delete('/delete/{id}',status_code=status.HTTP_200_OK)
async def delete_church(id: str, session: Session = Depends(get_session)):
    await church_controller.delete_church(church_id=id, session=session)
    return JSONResponse({'message': 'Deleted'})
