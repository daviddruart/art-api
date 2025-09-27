from fastapi import APIRouter, HTTPException
from models.art import Art
import services.art_service as art_service

router = APIRouter(prefix="/arts", tags=["Arts"])

@router.get("/")
def list_arts():
    return art_service.get_arts()

@router.get("/{art_id}")
def get_art(art_id: int):
    art = art_service.get_art_by_id(art_id)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return art

@router.post("/")
def add_art(art: Art):
    return art_service.create_art(art)

@router.put("/{art_id}")
def update_art(art_id: int, updated_art: Art):
    art = art_service.update_art(art_id, updated_art)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return art

@router.delete("/{art_id}")
def remove_art(art_id: int):
    art = art_service.delete_art(art_id)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return {"message": "Obra eliminada con éxito"}
