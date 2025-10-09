# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ruta del archivo SQLite (puedes cambiar el nombre si quieres)
SQLALCHEMY_DATABASE_URL = "sqlite:///./artcook.db"

# Conexión con SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sesión de trabajo con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
