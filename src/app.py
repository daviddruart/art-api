from fastapi import FastAPI
from config.database import Base, engine
from controllers import users_controller, art_controller
import models.user  # 👈 este import es clave

app = FastAPI(title="Art API - ArCook")

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(users_controller.router)
app.include_router(art_controller.router)
