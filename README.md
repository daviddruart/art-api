# ArCook API — FastAPI + SQLite + JWT

## Descripción general
ArCook es una versión extendida del proyecto original `art-api`, desarrollada en la rama `ArCook`.  
Su objetivo es ofrecer una API robusta para la gestión de obras de arte con autenticación de usuarios mediante JWT y almacenamiento en SQLite.  

La arquitectura sigue una estructura profesional con separación en controllers, services, schemas, models y config.

---

## Estructura del proyecto

```
art-api/
│
├── src/
│   └── app.py
│
├── config/
│   ├── auth.py
│   ├── database.py
│   └── dependencies.py
│
├── controllers/
│   ├── users_controller.py
│   └── art_controller.py
│
├── models/
│   ├── user.py
│   └── art.py
│
├── schemas/
│   ├── user_schema.py
│   └── art_schema.py
│
├── services/
│   ├── user_service.py
│   └── art_service.py
│
├── artcook.db
├── requirements.txt
└── README.md
```

---

## Pasos implementados en la rama `ArCook`

### 1. Creación de la rama
Desde Codespaces:
```bash
git checkout main
git pull origin main
git checkout -b ArCook
```

### 2. Instalación de dependencias
```bash
pip install fastapi uvicorn sqlalchemy pydantic passlib[bcrypt] python-jose[cryptography] python-dotenv email-validator
pip freeze > requirements.txt
```

### 3. Autenticación con JWT — `config/auth.py`
Se creó un sistema JWT para emisión y verificación de tokens.

### 4. Base de datos — `config/database.py`
Configuración de conexión con SQLite, con función `get_db()` para las sesiones de SQLAlchemy.

### 5. Modelo de usuario — `models/user.py`
Define el modelo `User` con los campos:
- id, username, email, password_hash, is_active

### 6. Esquemas de usuario — `schemas/user_schema.py`
Define los modelos Pydantic para:
- Registro (UserCreate)
- Login (UserLogin)
- Respuesta (UserOut)

### 7. Lógica de usuario — `services/user_service.py`
Implementación de:
- Hashing con bcrypt
- Validación de contraseñas
- Creación y autenticación de usuarios
- Generación de token JWT

### 8. Controlador de usuarios — `controllers/users_controller.py`
Endpoints creados:
- POST /users/register → Registrar usuario  
- POST /users/login → Iniciar sesión y obtener token JWT

### 9. Esquemas de arte — `schemas/art_schema.py`
Define los modelos:
- ArtCreate, ArtUpdate, ArtResponse

### 10. Dependencias — `config/dependencies.py`
Función get_current_user() para proteger rutas mediante token JWT.

### 11. Controlador de arte — `controllers/art_controller.py`
CRUD completo de obras de arte:
- GET /arts → público  
- GET /arts/{id} → público  
- POST /arts → protegido con token  
- PUT /arts/{id} → protegido  
- DELETE /arts/{id} → protegido  

Integración de:
```python
current_user: User = Depends(get_current_user)
```

### 12. Integración en `src/app.py`
Registro de routers y creación automática de tablas:
```python
from config.database import Base, engine
from controllers import users_controller, art_controller
import models.user

Base.metadata.create_all(bind=engine)
app.include_router(users_controller.router)
app.include_router(art_controller.router)
```

### 13. Solución de errores encontrados

| Error | Causa | Solución |
|-------|--------|----------|
| ModuleNotFoundError: No module named 'schemas.art_schema' | Faltaba archivo `art_schema.py` | Se creó el esquema completo |
| ValueError: password cannot be longer than 72 bytes | Incompatibilidad de bcrypt | Se reinstaló bcrypt==4.0.1 y passlib==1.7.4 |
| 500 Internal Server Error | Tabla `users` no creada | Se importó `models.user` en `src/app.py` |
| 404 Not Found | Swagger abierto fuera del puerto 8000 | Se usó correctamente `https://<codespace>-8000.app.github.dev/docs` |

### 14. Verificación final

1. Registro de usuario (POST /users/register):
```json
{
  "username": "artlover",
  "email": "artlover@example.com",
  "password": "123456"
}
```

2. Login (POST /users/login):
```json
{
  "username": "artlover",
  "password": "123456"
}
```
Respuesta:
```json
{
  "access_token": "<TOKEN>",
  "token_type": "bearer"
}
```

3. En Swagger, usar el botón Authorize y pegar:
```
Bearer <TOKEN>
```

4. Endpoints de arte (requieren token para POST/PUT/DELETE).

---

## Requisitos mínimos
- Python 3.10+
- FastAPI 0.110+
- SQLite 3.x
- GitHub Codespaces (o entorno local con VSCode)

---

## Ejecución

```bash
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

Abrir en navegador:
```
https://<tu-codespace>-8000.app.github.dev/docs
```

---

## Licencia
Proyecto desarrollado por Cristian David Rincón Urrea como extensión educativa y experimental de `art-api`, bajo fines de aprendizaje y desarrollo profesional.
