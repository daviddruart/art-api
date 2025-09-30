#  Art API

API RESTful construida con **FastAPI** y **SQLite** para la gestión de obras de arte.  
Este proyecto fue desarrollado desde cero en **GitHub Codespaces**, siguiendo buenas prácticas con **SQLAlchemy** y **Pydantic**.

---

##  Características
- CRUD completo de obras de arte:
  - Crear (`POST /arts/`)
  - Listar (`GET /arts/`)
  - Obtener por ID (`GET /arts/{id}`)
  - Actualizar (`PUT /arts/{id}`)
  - Eliminar (`DELETE /arts/{id}`)
- Base de datos persistente con **SQLite** (`arts.db`).
- Validación de datos con **Pydantic** (schemas).
- Documentación automática con **Swagger UI** (`/docs`) y **ReDoc** (`/redoc`).

---

##  Tecnologías utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) – framework web rápido y moderno.
- [Uvicorn](https://www.uvicorn.org/) – servidor ASGI.
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM para manejar la base de datos.
- [SQLite](https://www.sqlite.org/) – base de datos ligera.
- [Pydantic](https://docs.pydantic.dev/) – validación de datos.

---

##  Estructura del proyecto
    art-api/
    ├── config/ # Configuración de la base de datos
    │ └── database.py
    ├── controllers/ # Rutas / endpoints de la API
    │ └── art_controller.py
    ├── models/ # Modelos de la base de datos
    │ └── art.py
    ├── schemas/ # Esquemas Pydantic para validación/response
    │ └── art_schema.py
    ├── services/ # Lógica de negocio y conexión con la BD
    │ └── art_service.py
    ├── src/ # Punto de entrada de la aplicación
    │ └── app.py
    ├── requirements.txt # Dependencias del proyecto
    └── README.md # Este archivo 
## Crear entorno virtual
    python -m venv venv
    venv\Scripts\activate 
## Instalar dependencias
    pip install -r requirements.txt
## Levantar el servidor
    uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
El servidor se ejecutará en:
 http://localhost:8000 (local)
 En Codespaces: https://<tu-codespace>-8000.app.github.dev

# Ejemplos de uso (curl)
## Crear obra
    curl -X POST "http://localhost:8000/arts/" \
      -H "Content-Type: application/json" \
      -d '{
        "title":"La noche estrellada",
        "artist":"Vincent van Gogh",
        "year":1889,
        "style":"Postimpresionismo",
        "description":"Óleo sobre lienzo"
      }'
## Lista de obras
    curl "http://localhost:8000/arts/"
## Obtener obras por ID
    curl "http://localhost:8000/arts/1"
## Actualizar obra
    curl -X PUT "http://localhost:8000/arts/1" \
      -H "Content-Type: application/json" \
      -d '{"style":"Postimpresionismo - actualizado", "year":1890}'
## Eliminar obra
    curl -X DELETE "http://localhoost:8000/arts/1"



## Próximos pasos / mejoras

- Agregar autenticación de usuarios.

- Migrar la base de datos a MySQL o PostgreSQL.

- Crear un frontend en React que consuma esta API.

- Poblar con dataset de obras de usuarios.



