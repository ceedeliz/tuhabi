from fastapi import APIRouter
from app.core.src.endpoints import property

router = APIRouter()
router.include_router(property.router)
