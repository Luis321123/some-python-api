from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.controller.church_user import ChurchUserUpdate, ChurchUserCreate
from app.controller.church_user import church_user

router = APIRouter()

@router.post("/create/", response_model=ChurchUserCreate, status_code=status.HTTP_201_CREATED)
async def create_church_user(user: ChurchUserCreate, session: Session = Depends(get_session)):
    new_user = await church_user.create_church_user(data=user, session=session)
    return JSONResponse(content=new_user, status_code=status.HTTP_201_CREATED)

@router.get("/get/{user_uuid}", status_code=status.HTTP_200_OK)
async def get_church_user_session(user_uuid: str, session: Session = Depends(get_session)):
    church_user_get = await church_user.get_church_user(user_uuid=user_uuid, db=session)
    return church_user_get

@router.get("/get_all/{church_uuid}", status_code=status.HTTP_200_OK)
async def get_church_users(church_uuid: str, session: Session = Depends(get_session)):
    church_users = await church_user.get_church_users_by_church(church_uuid=church_uuid, db=session)
    return church_users

@router.put("/update/{user_uuid}", status_code=status.HTTP_200_OK)
async def update_church_user_session(user_uuid: str, data: ChurchUserUpdate, session: Session = Depends(get_session)):
    await church_user.update_church_user(user_uuid=user_uuid, data=data, db=session)
    return JSONResponse({'message': 'updated'})

@router.delete("/delete/{church_user_uuid}", status_code=status.HTTP_200_OK)
async def delete_church_user(church_user_uuid: str, session: Session = Depends(get_session)):
    await church_user.delete_church_user(user_uuid=church_user_uuid, session=session)
    return JSONResponse({'message': 'Deleted'})

