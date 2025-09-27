from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.art import Art
import services.art_service as art_service
from config.database import SessionLocal

router = APIRouter(prefix="/arts", tags=["Arts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_arts(db: Session = Depends(get_db)):
    return art_service.get_arts(db)

@router.get("/{art_id}")
def get_art(art_id: int, db: Session = Depends(get_db)):
    art = art_service.get_art_by_id(db, art_id)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return art

@router.post("/")
def add_art(title: str, artist: str, year: int, style: str = None, description: str = None, db: Session = Depends(get_db)):
    new_art = Art(title=title, artist=artist, year=year, style=style, description=description)
    return art_service.create_art(db, new_art)

@router.delete("/{art_id}")
def remove_art(art_id: int, db: Session = Depends(get_db)):
    art = art_service.delete_art(db, art_id)
    if not art:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    return {"message": "Obra eliminada con éxito"}
