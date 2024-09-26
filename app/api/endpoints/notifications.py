from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.controller.notifications import send_notification
router = APIRouter()

notification_controller = NotificationController()

@router.post("/notifications")
async def create_notification(notification: NotificationCreate, db: Session = Depends(get_session)):
    return notification_controller.send_notification(
        title=notification.title,
        content=notification.content,
        image=notification.image,
        token=notification.token,
        data=notification.data
    )





#@router.get("/get/{user_uuid}", status_code=status.HTTP_200_OK)
#async def get_church_user_session(user_uuid: str, session: Session = Depends(get_session)):
    #church_user_get = await church_user.get_church_user(user_uuid=user_uuid, db=session)
    #return church_user_get