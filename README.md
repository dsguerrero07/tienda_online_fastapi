# Tienda Online - FastAPI

Proyecto desarrollado con **FastAPI + SQLModel**, que gestiona productos y categorías con lógica de negocio, validaciones y documentación automática.

---

## Funcionalidades principales

- Registrar **categorías** (nombre, descripción)
- Registrar **productos** (nombre, precio, stock, descripción)
- Cada producto pertenece a **una categoría**
- Consulta de productos por categoría
- Gestión de stock (sin valores negativos)
- Activación/Desactivación de categorías y productos
- Listado de categorías y productos activos e inactivos
- Recuperación de categorías y productos desactivados
- Filtros por categoría y nivel de stock

---

## Tecnologías

- Python 3.13
- FastAPI
- SQLModel
- Uvicorn
- Pydantic

---

## Endpoints Principales 

- Get "/" mensaje de bienvenida
- POST "/categoria/" crear categoria 
- GET "/categorias/" Listar categorías activas
- GET "/categorias/desactivadas" Listar categorías desactivadas
- PUT "/categorias/{id}" Actualizar categoría
- DELETE "/categorias/{id}" Desactivar categoría
- PUT "/categorias/{id}/recuperar" Reactivar categoría
- POST "/productos/" Crear producto
- GET  "/productos/" Listar productos activos
- GET "/productos/desactivados" Listar productos desactivados
- PUT "/productos/{id}" Actualizar producto
- DELETE "/productos/{id}" Desactivar producto
- PUT "/productos/{id}/recuperar" Reactivar producto

---

##  Instalación y ejecución

###  Clonar el repositorio
```bash
git clone https://github.com/dsguerrero07/tienda_online_fastapi.git
cd tienda_online_fastapi
