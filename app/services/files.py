from sqlalchemy.orm import Session
import logging

from app.services.base import CRUDBase
from app.models.Files import Files
from app.schemas.File import FileSave, FileInDBBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ServiceFiles(CRUDBase[Files, FileSave, FileSave]):
    async def read_file(self, db: Session, file_id: str):
        try:
            if not file_id:
                raise 'The id determinted isnt found'
            return self.get(db=db, id=file_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise f'There is a error: {str(ex)}'

    async def create_file(self, db: Session, *, user_id: str, obj_in, agency_id: str | None = None) -> FileInDBBase:
        try:
            db_obj = self.model(
                user_id=user_id,
                agency_id=agency_id,
                **obj_in
            )
            file_current = self.create(db=db, obj_in=db_obj)
            return file_current
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise f'There is a error: {str(ex)}'

    async def remove_file(self, db: Session, file_id: str):
        try:
            self.remove(db=db, id=file_id)
        except Exception as ex:
            logger.error(f"Unexpected Error: {str(ex)}")
            raise f'There is a error: {str(ex)}'

serviceFile = ServiceFiles(Files)