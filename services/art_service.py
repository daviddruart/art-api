from sqlalchemy.orm import Session
from models.art import Art
from config.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_arts(db: Session):
    return db.query(Art).all()

def get_art_by_id(db: Session, art_id: int):
    return db.query(Art).filter(Art.id == art_id).first()

def create_art(db: Session, art: Art):
    db.add(art)
    db.commit()
    db.refresh(art)
    return art

def delete_art(db: Session, art_id: int):
    art = db.query(Art).filter(Art.id == art_id).first()
    if art:
        db.delete(art)
        db.commit()
    return art

