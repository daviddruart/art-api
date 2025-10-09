# src/app.py
from fastapi import FastAPI
from config.database import Base, engine
from controllers import users_controller
import models.user  # asegúrate de importar para crear la tabla

# Crear la app
app = FastAPI(title="Art API - ArCook")

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir los routers
app.include_router(users_controller.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Arte - Rama ArCook 🎨"}
