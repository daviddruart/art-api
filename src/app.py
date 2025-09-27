from fastapi import FastAPI
from controllers import art_controller

app = FastAPI(title="Art API")

# incluir rutas del controlador
app.include_router(art_controller.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a Artelleria"}