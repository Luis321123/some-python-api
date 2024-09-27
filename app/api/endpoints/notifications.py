from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.controller.notifications import send_notification


router = APIRouter()



@router.post("/notifications", status_code=status.HTTP_201_CREATED)
async def create_notification(title: str, content: str, image: str, token: str, data: dict = None, db: Session = Depends(get_session)):
    await send_notification(title, content, image, token, data)
    return JSONResponse({'message': 'created'})

