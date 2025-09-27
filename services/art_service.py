from models.art import Art

# "Base de datos" tempporal en memoria
arts_db = []

def get_arts():
    return arts_db

def get_art_by_id(art_id: int):
    return next((art for art in arts_db if art.id == art_id), None)

def cretae_art(art: Art):
    arts_db.append(art)
    return art

def update_art(art_id: int, updated_art: Art):
    for i, art in enumerate(arts_db):
        if art.id == art_id:
            arts_db[i] = updated_art
            return updated_art
    return None

def delete_art(art_id: int):
    for i, art in enumerate(arts_db):
        if art.id == art_id:
            return arts_db.pop(i)
    return None
