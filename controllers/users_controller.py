from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate, UserLogin, UserOut
from services import user_service
from config.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

# ---- Registro de usuario ----
@router.post("/register", response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = user_service.get_user_by_username(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe.")
    new_user = user_service.create_user(
        db, user_data.username, user_data.email, user_data.password
    )
    return new_user

# ---- Inicio de sesión ----
@router.post("/login")
def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    token_data = user_service.login_user(db, user_data.username, user_data.password)
    if not token_data:
        raise HTTPException(status_code=401, detail="Credenciales inválidas.")
    return token_data
