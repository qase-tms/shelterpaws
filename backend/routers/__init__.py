from backend.routers.animal_router import router as animals_router
from backend.routers.animal_photo_router import router as animals_photo_router

routes = [
    animals_router,
    animals_photo_router
]
