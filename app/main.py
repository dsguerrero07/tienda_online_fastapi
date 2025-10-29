from fastapi import FastAPI
from app.db import crear_db
from app.routes import categoria_routes, producto_routes

app = FastAPI(title="Tienda Online FastAPI")

crear_db()  # crea la base de datos al iniciar

# incluir las rutas
app.include_router(categoria_routes.router)
app.include_router(producto_routes.router)

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de la Tienda Online"}
