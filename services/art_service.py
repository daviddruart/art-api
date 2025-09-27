from sqlalchemy.orm import Session
from models.art import Art

def get_arts(db: Session):
    return db.query(Art).all()

def get_art_by_id(db: Session, art_id: int):
    return db.query(Art).filter(Art.id == art_id).first()

def create_art(db: Session, art_data: dict):
    art = Art(**art_data)
    db.add(art)
    db.commit()
    db.refresh(art)
    return art

def update_art(db: Session, art_id: int, updated_data: dict):
    art = get_art_by_id(db, art_id)
    if not art:
        return None
    # solo setea campos provistos (exclude_unset en controller)
    for key, value in updated_data.items():
        if value is not None and hasattr(art, key):
            setattr(art, key, value)
    db.commit()
    db.refresh(art)
    return art

def delete_art(db: Session, art_id: int):
    art = get_art_by_id(db, art_id)
    if art:
        db.delete(art)
        db.commit()
    return art