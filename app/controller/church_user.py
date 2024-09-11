
from app.schemas.user import ChurchUser, ChurchUserCreate, ChurchUserUpdate
from app.services.base import CRUDBase


class ChurchUserController(CRUDBase[ChurchUser, ChurchUserCreate, ChurchUserUpdate]):
    pass



church_user = ChurchUserController(ChurchUser)
    