from fastapi import FastAPI
from controllers import art_controller

app = FastAPI(title="Art API")

app.include_router(art_controller.router)


@app.get("/")
def root():
    return {"Bienvenido a Artelleria"}