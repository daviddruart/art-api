# config/auth.py
from datetime import datetime, timedelta
from jose import jwt, JWTError

# Clave secreta (puedes cambiarla o leerla desde .env)
SECRET_KEY = "superclaveultrasecreta123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Duración del token

# Crear un token de acceso (al iniciar sesión)
def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Verificar y decodificar un token recibido
def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
