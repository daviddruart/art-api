from pydantic import BaseModel
from typing import Optional

class Art(BaseModel):
    id: int
    title: str
    artist: str
    year: int 
    style: Optional[str] = None
    description: Optional[str] = None