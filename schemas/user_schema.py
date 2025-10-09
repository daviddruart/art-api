# schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional

# Datos requeridos para registrar un nuevo usuario
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Datos que se devuelven al consultar un usuario
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True

# Datos que se envían para iniciar sesión
class UserLogin(BaseModel):
    username: str
    password: str
