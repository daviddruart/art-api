from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from controllers import users_controller, art_controller
import models.user  # 👈 este import es clave

app = FastAPI(title="Art API - ArCook")

# Configurar CORS para permitir conexión con el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Puerto del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(users_controller.router)
app.include_router(art_controller.router)
