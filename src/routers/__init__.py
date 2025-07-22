from aiogram import Router
from .start import router as start_router
from .c1 import router as c1_router
from .complaints import router as complaints_router
from .base import router as base_router
from .wait import router as wait_router
from .enclosure import router as enclosure_router

router = Router(name=__name__)
router.include_routers(
    start_router,
    c1_router,
    complaints_router,
    base_router,
    wait_router,
    enclosure_router,
)
