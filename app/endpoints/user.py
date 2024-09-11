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
from app.controller.user import user as user_controller
from app.schemas.user import UserCreate

router=APIRouter()


@router.post('/create/{id}', status_code=status.HTTP_201_CREATED)
async def user_create(id: str, data:UserCreate, session: Session = Depends(get_session)):
    await user_controller.create_user(church_id=id, data=data, session=session)
    return JSONResponse(user_controller)

