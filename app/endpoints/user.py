import logging

from fastapi import APIRouter, Depends, UploadFile, status, Query, HTTPException, BackgroundTasks, Query
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from typing import Optional, List

from datetime import datetime

from app import services
from app.core.security import get_current_user
from app.core.database import get_session
from app.schemas.church import ChurchCreate


router = APIRouter()


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_church(data:ChurchCreate, session: Session = Depends(get_session)):
    pass
