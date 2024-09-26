from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.services.base import CRUDBase
from app.schemas.church_user import ChurchUserCreate, ChurchUserUpdate
from app.models.ChurchUsers import ChurchUsers
from app.schemas.church_user import ChurchUserCreate

class ChurchUserController(CRUDBase[ChurchUsers, ChurchUserCreate, ChurchUserUpdate,]):
    async def create_church_user(self, data: ChurchUserCreate, session: Session):
        try:
            self.create(db=session, obj_in=data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
   
    async def get_church_user(self, user_uuid: str, db: Session):
        church_user = db.query(self.model).filter(self.model.uuid == user_uuid).first()
        if not church_user:
            raise HTTPException(status_code=404, detail="Usuario de la iglesia no encontrado.")
        return church_user
    
    async def update_church_user(self, user_uuid: str, data: ChurchUserUpdate, db: Session):
        try:
            church_user = await self.get_church_user(db=db, id=user_uuid)
            
            if not church_user:
                raise HTTPException(status_code=404, detail="Usuario de la iglesia no encontrado.")
            
            self.update(db=db, db_obj=church_user, obj_in=data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
        return church_user
    
    async def delete_church_user(self, user_uuid: str, session: Session):
        try:
            self.remove(db=session, uuid=user_uuid)
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
        
    async def get_church_users_by_church(self, church_uuid: str, db: Session):
        church_users = db.query(self.model).filter(self.model.church_uuid == church_uuid).all()
        if not church_users:
            raise HTTPException(status_code=404, detail="No se encontraron usuarios para esta iglesia.")
        return church_users
        

church_user = ChurchUserController(ChurchUsers)
