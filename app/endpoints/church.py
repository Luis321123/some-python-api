import logging
from fastapi import FastAPI
from fastapi import APIRouter, Depends, UploadFile, status, Query, HTTPException, BackgroundTasks, Query
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from typing import Optional, List

from datetime import datetime

from app import services
from app.core.security import get_current_user
from app.core.database import get_session
from app.schemas.church import ChurchCreate, ChurchUpdate, ChurchInDB


router = APIRouter()

@router.get('/me/{id}',status_code=status.HTTP_200_OK)
async def get_church(id: str, session: Session = Depends(get_session)):
    pass

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_church(data:ChurchCreate, session: Session = Depends(get_session)):
    pass

@router.put('update/{id}', status_code=status.HTTP_200_OK)
async def update_church(id: str, data: ChurchUpdate, session: Session = Depends(get_session)):
    pass

@router.put('/delete/{id}',status_code=status.HTTP_200_OK)
async def delete_church(id: str, session: Session = Depends(get_session)):
    pass