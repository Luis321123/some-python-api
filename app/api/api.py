from fastapi import APIRouter, Depends


from app.api.endpoints.church_user import router as router_church_user
from app.api.endpoints.auth import router as router_auth
from app.api.endpoints.church import router as router_church
from app.api.endpoints.user import router as router_user
from app.api.endpoints.debug import router as router_debug
from app.api.endpoints.health_check import router as router_check
from app.api.deps import get_current_user, get_current_is_superuser

api_router = APIRouter()
#router auth
api_router.include_router(router_auth, prefix="/auth", tags=["Auth"],
    responses={404: {"description": "Not found"}})
#routes debug
api_router.include_router(router_debug, prefix="/debug", tags=["Debug"],
    responses={404: {"description": "Not found"}})
    
#routes church
api_router.include_router(router_church, prefix="/church", tags=["Church"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_is_superuser)])
#router user
api_router.include_router(router_user, prefix="/user", tags=["User"],
 responses={404: {"description": "Not found"}},
 dependencies=[Depends(get_current_user)])
#routes church_user
api_router.include_router(router_church_user, prefix="/churchUser", tags=["Church_user"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)])
#route Checkout
api_router.include_router(router_check, prefix="/checkout", tags=["HealthCheck"],
    responses={404: {"description": "Not found"}})

