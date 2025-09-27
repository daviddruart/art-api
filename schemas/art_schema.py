from pydantic import BaseModel, Field
from typing import Optional

# ---- Schema base (campos comunes) ----
class ArtBase(BaseModel):
    title: str = Field(..., example="La noche estrellada")
    artist: str = Field(..., example="Vincent van Gogh")
    year: Optional[int] = Field(None, example=1889)
    style: Optional[str] = Field(None, example="Postimpresionismo")
    description: Optional[str] = Field(None, example="Óleo sobre lienzo.")

# ---- Para crear una obra ----
class ArtCreate(ArtBase):
    pass

# ---- Para actualizar (todos opcionales) ----
class ArtUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    year: Optional[int] = None
    style: Optional[str] = None
    description: Optional[str] = None

# ---- Para responder (incluye id) ----
class ArtResponse(ArtBase):
    id: int

    class Config:
        orm_mode = True
