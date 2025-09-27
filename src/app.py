from fastapi import FastAPI
from controllers import art_controller
from config.database import Base, engine
import models.art

#crea las tablas en la BD
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Art API")

app.include_router(art_controller.router)


@app.get("/")
def root():
    return {"Bienvenido a Artelleria"}