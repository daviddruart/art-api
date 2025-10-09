# controllers/art_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.art_schema import ArtCreate, ArtUpdate
from services import art_service
from models.art import Art
from config.dependencies import get_current_user  
from models.user import User  # para tipar el usuario actual

router = APIRouter(prefix="/arts", tags=["Arts"])


@router.get("/")
def get_arts(db: Session = Depends(get_db)):
    return art_service.get_arts(db)


@router.get("/{art_id}")
def get_art(art_id: int, db: Session = Depends(get_db)):
    art = art_service.get_art_by_id(db, art_id)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada.")
    return art


@router.post("/")
def create_art(
    art_data: ArtCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user contiene el usuario que está logueado
    print(f"✅ Usuario autenticado: {current_user.username}")
    new_art = art_service.create_art(db, art_data)
    return {"message": "Obra creada correctamente", "art": new_art}


@router.put("/{art_id}")
def update_art(
    art_id: int,
    art_data: ArtUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = art_service.update_art(db, art_id, art_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Obra no encontrada.")
    return {"message": "Obra actualizada correctamente", "art": updated}


@router.delete("/{art_id}")
def delete_art(
    art_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = art_service.delete_art(db, art_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Obra no encontrada.")
    return {"message": "Obra eliminada correctamente"}
