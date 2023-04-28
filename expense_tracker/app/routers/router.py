from fastapi import APIRouter

from app.routers.health import router as health_router
from app.routers.auth import router as auth_router
from app.routers.budget import router as budget_router

router = APIRouter()
router.include_router(health_router, prefix="/health", tags=["Service health"])
router.include_router(auth_router, prefix="/auth", tags=["Service auth"])
router.include_router(budget_router, prefix="/budget", tags=["Budget"])
