# services/user_service.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user import User
from config.auth import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    # 🔒 asegurarse de que sea string y corto
    password = str(password)[:72]
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(str(plain_password)[:72], hashed_password)

def create_user(db: Session, username: str, email: str, password: str):
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

def login_user(db: Session, username: str, password: str):
    user = authenticate_user(db, username, password)
    if not user:
        return None
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
