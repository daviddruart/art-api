from pydantic import BaseModel, Field
from typing import Optional

class ArtBase(BaseModel):
    title: str = Field(..., example="La noche estrellada")
    artist: str = Field(..., example="Vincent van Gogh")
    year: Optional[int] = Field(None, example=1889)
    style: Optional[str] = Field(None, example="Postimpresionismo")
    description: Optional[str] = Field(None, example="Óleo sobre lienzo.")

class ArtCreate(ArtBase):
    pass

class ArtUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    year: Optional[int] = None
    style: Optional[str] = None
    description: Optional[str] = None

class ArtResponse(ArtBase):
    id: int

    class Config:
        orm_mode = True