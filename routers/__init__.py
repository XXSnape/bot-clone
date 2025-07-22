from aiogram import Router
from .start import router as start_router
from .c1 import router as c1_router

router = Router(name=__name__)
router.include_routers(start_router, c1_router)
