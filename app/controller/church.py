from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.church import ChurchCreate, ChurchUpdate
from app.services.base import CRUDBase
from app.models.Churches import Churches

class ChurchController(CRUDBase[Churches, ChurchCreate, ChurchUpdate]):
    async def get_church(self, db:Session, id: str):
        church = await db.query(self.model).filter(self.model.uuid == id).first()
        if not church:
            raise HTTPException(status_code=404, detail="Iglesia no encontrada.")
        return church

    async def update_church(self, data: ChurchUpdate, church_id: str, session: Session):
        try:
            # obtener modelo
            church_current = await self.get_church(db=session, id=church_id)
            
            self.update(db=session, db_obj=church_current, obj_in=data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

    async def create_church(self, data: ChurchCreate, session: Session):
        try:
            self.create(db=session, obj_in=data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

    async def delete_church(self, church_id:str, session: Session):
        try:
            self.remove(db=session, id=church_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")



church=ChurchController(Churches)