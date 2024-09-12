from app.api.endpoints import auth as router_auth

api_router = APIRouter()

api_router.include_router(router_auth, prefix="/auth", tags=["Auth"],
    responses={404: {"description": "Not found"}})