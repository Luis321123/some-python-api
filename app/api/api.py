from fastapi import APIRouter


from app.api.endpoints import auth as router_auth
from app.api.endpoints import church as router_church
from app.api.endpoints import user as router_user


api_router = APIRouter()

api_router.include_router(router_auth, prefix="/auth", tags=["Auth"],
    responses={404: {"description": "Not found"}})

api_router.include_router(router_church, prefix="/church", tags=["Church"],
    responses={404: {"description": "Not found"}})

api_router.include_router(router_user, prefix="/user", tags=["User"],
    responses={404: {"description": "Not found"}})
