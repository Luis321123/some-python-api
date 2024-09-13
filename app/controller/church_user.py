from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.services.base import CRUDBase
from app.schemas.church_user import ChurchUserCreate, ChurchUserUpdate
from app.models.ChurchUsers import ChurchUsers
from app.schemas.church_user import ChurchUserCreate

class ChurchUserController(CRUDBase[ChurchUsers, ChurchUserCreate, ChurchUserUpdate]):
    async def create_church_user(self, data: ChurchUserCreate, session: Session):
        try:
            self.create(db=session, obj_in=data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

church_user = ChurchUserController(ChurchUsers)