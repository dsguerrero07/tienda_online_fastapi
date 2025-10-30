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
- Filtros por precio, stock y categoría

---

## Tecnologías

- Python 3.13
- FastAPI
- SQLModel
- Uvicorn
- Pydantic

---

##  Instalación y ejecución

###  Clonar el repositorio
```bash
git clone https://github.com/dsguerrero07/tienda_online_fastapi.git
cd tienda_online_fastapi
