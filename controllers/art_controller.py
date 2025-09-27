from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from config.database import SessionLocal
import services.art_service as art_service
from schemas.art_schema import ArtCreate, ArtUpdate, ArtResponse

router = APIRouter(prefix="/arts", tags=["Arts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ArtResponse])
def list_arts(db: Session = Depends(get_db)):
    return art_service.get_arts(db)

@router.get("/{art_id}", response_model=ArtResponse)
def get_art(art_id: int, db: Session = Depends(get_db)):
    art = art_service.get_art_by_id(db, art_id)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return art

@router.post("/", response_model=ArtResponse, status_code=201)
def add_art(art_in: ArtCreate, db: Session = Depends(get_db)):
    art = art_service.create_art(db, art_in.dict())
    return art

@router.put("/{art_id}", response_model=ArtResponse)
def update_art(art_id: int, art_in: ArtUpdate, db: Session = Depends(get_db)):
    # exclude_unset para que solo los campos enviados se apliquen
    data = art_in.dict(exclude_unset=True)
    art = art_service.update_art(db, art_id, data)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return art

@router.delete("/{art_id}", status_code=200)
def remove_art(art_id: int, db: Session = Depends(get_db)):
    art = art_service.delete_art(db, art_id)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return {"message": "Obra eliminada con éxito"}