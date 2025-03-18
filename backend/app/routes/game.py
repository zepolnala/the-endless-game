from fastapi import APIRouter
from app.services.story_generator import generate_story
from app.services.image_generator import generate_image
from pydantic import BaseModel

# Crear el enrutador
router = APIRouter()

# Definir el modelo de datos para recibir entradas del usuario
class UserInput(BaseModel):
    user_id: str
    message: str

# Endpoint para generar historia con IA
@router.post("/generate-story")
def generate_story_route(user_input: UserInput):
    return generate_story(user_input.message)

# Endpoint para generar checkpoint (imagen)
@router.post("/generate-checkpoint")
def generate_checkpoint_route(user_input: UserInput):
    return generate_image(user_input.message)
