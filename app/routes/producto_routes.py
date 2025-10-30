from fastapi import APIRouter , HTTPException , status
from sqlmodel import Session , select
from app.db import engine
from app.models.producto import Producto
from app.models.categoria import Categoria

router = APIRouter(prefix="/productos", tags=["Productos"])

#crear producto
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(producto: Producto):
    with Session(engine) as session:
        categoria = session.get(Categoria, producto.categoria_id)
        if not categoria.activa:
            raise HTTPException(status_code=400, detail="La categoría no existe")

        if producto.stock < 0:
            raise HTTPException(status_code=400, detail="El stock no puede ser negativo")

        session.add(producto)
        session.commit()
        session.refresh(producto)
        return producto

#listar productos con filtro
@router.get("/")
def listar_productos():
    with Session(engine) as session:
        consulta = select(Producto).where(Producto.activo == True)
        if categoria_id:
            consulta = consulta.where(Producto.categoria_id == categoria_id)
        if min_stock:
            consulta = consulta.where(Producto.stock >= min_stock)

        productos = session.exec(consulta).all()
        return productos
    
#obtener producto con su categoria
@router.get("/{producto_id}")
def obtener_producto(producto_id: int):
    with Session(engine) as session:
        producto = session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return producto

#actualizar producto
@router.put("/{producto_id}")  
def actualizar_producto(producto_id: int, datos: Producto):
    with Session(engine) as session:
        producto = session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        if datos.stock < 0:
            raise HTTPException(status_code=400, detail="El stock no puede ser negativo")

        producto.nombre = datos.nombre
        producto.precio = datos.precio
        producto.stock = datos.stock
        producto.descripcion = datos.descripcion
        producto.categoria_id = datos.categoria_id
        session.commit()
        session.refresh(producto)
        return producto
    
# Desactivar producto
@router.delete("/{producto_id}")
def desactivar_producto(producto_id: int):
    with Session(engine) as session:
        producto = session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        producto.activo = False
        session.commit()
        return {"mensaje": "Producto desactivado correctamente"}

#listar productos desactivados
@router.get("/desactivados")
def listar_productos_desactivados():
    with Session(engine) as session:
        productos=session.exec(select(Producto).where(Producto.activo==False)).all()
        return productos
#recuperar producto desactivado
@router.post("/recuperar/{producto_id}")
def recuperar_producto(producto_id: int):
    with Session(engine) as session:
        producto = session.get(Producto, producto_id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        if producto.activo:
            raise HTTPException(status_code=400, detail="El producto ya está activo")

        producto.activo = True
        session.commit()
        session.refresh(producto)
        return {"mensaje": "Producto recuperado correctamente"}