from fastapi import FastAPI
from app.routes.game import router
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Instancia de FastAPI
app = FastAPI()

# Incluir las rutas del juego
app.include_router(router)

@app.get("/")
def root():
    return {"message": "The Endless Game Backend is Running!"}
