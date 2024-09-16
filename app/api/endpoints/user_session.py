from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

router= APIRouter()

from app.core.database import get_session
from app.controller.auth import auth as auth_controller

