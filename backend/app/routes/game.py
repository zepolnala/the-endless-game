from fastapi import APIRouter
from pydantic import BaseModel
from app.services.story_generator import generate_story  # Asegúrate de que este import es correcto

router = APIRouter()

# 🔹 Definir la clase StoryRequest (Pydantic)
class StoryRequest(BaseModel):
    user_id: str
    message: str

@router.post("/generate-story")
def generate_story_route(user_input: StoryRequest):
    return generate_story(user_input.message)

@router.post("/generate-checkpoint")
def generate_checkpoint_route(user_input: StoryRequest):
    return {"message": "Checkpoint generado para " + user_input.user_id}
