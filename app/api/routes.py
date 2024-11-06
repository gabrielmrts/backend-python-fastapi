from app.api.controllers import session
from fastapi.routing import APIRouter

router = APIRouter()
router.include_router(session.router)
