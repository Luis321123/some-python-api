from fastapi import APIRouter
router = APIRouter()

@router.get("/healthcheck", tags=["Healthcheck"])
async def healthcheck():
    return "alive"
