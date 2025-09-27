from fastapi import FastAPI
from controllers import art_controller

app = FastAPI(title="Art API")

app.include_router(art_controller.router)

# crea tablas en startup (asegúrate de importar el modelo para que se registre)
from config.database import Base, engine
import models.art  # importa el modelo para que Base conozca la tabla
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Arte 🎨"}
