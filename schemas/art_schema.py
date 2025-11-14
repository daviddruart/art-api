# schemas/art_schema.py
from pydantic import BaseModel
from typing import Optional

# ✅ Modelo para crear una nueva obra
class ArtCreate(BaseModel):
    title: str
    artist: str
    description: Optional[str] = None
    year: Optional[int] = None

# ✅ Modelo para actualizar una obra
class ArtUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None

# ✅ Modelo de respuesta
class ArtResponse(BaseModel):
    id: int
    title: str
    artist: str
    description: Optional[str]
    year: Optional[int]

    class Config:
        orm_mode = True
