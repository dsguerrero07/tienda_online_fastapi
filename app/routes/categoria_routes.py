from fastapi import APIRouter, HTTPException , status
from sqlmodel import Session, select
from app.db import engine
from app.models.categoria import Categoria
from app.schemas.categoria_schema import CategoriaCreate, CategoriaOut , CategoriaUpdate

router = APIRouter(prefix="/categorias", tags=["Categorias"])

#crear categoria
@router.post("/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: CategoriaCreate):
    with Session(engine) as session:
        existente = session.exec(select(Categoria).where(Categoria.nombre == categoria.nombre)).first()
        if existente:
            raise HTTPException(status_code=409, detail="El nombre de la categoría ya existe")

        nueva = Categoria(**categoria.model_dump())
        session.add(nueva)
        session.commit()
        session.refresh(nueva)
        return nueva

#listar categorias
@router.get("/",status_code=status.HTTP_201_CREATED)
def listar_categorias():
    with Session(engine) as session:
        categorias=session.exec(select(Categoria).where(Categoria.activa==True)).all()
        return categorias

#obtener categoria con su productos
@router.get("/{categoria_id}")
def obtener_categoria(categoria_id: int):
    with Session(engine) as session:
        categoria = session.get(Categoria, categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return categoria
    
#actualizar categoria
@router.put("/{categoria_id}")
def actualizar_categoria(categoria_id: int, datos: Categoria):
    with Session(engine) as session:
        categoria = session.get(Categoria, categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        
        categoria.nombre = datos.nombre
        categoria.descripcion = datos.descripcion
        session.commit()
        session.refresh(categoria)
        return categoria

# Desactivar categoría
@router.delete("/{categoria_id}")
def desactivar_categoria(categoria_id: int):
    with Session(engine) as session:
        categoria = session.get(Categoria, categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")

        categoria.activa = False
        session.commit()
        return {"mensaje": "Categoría desactivada correctamente"}