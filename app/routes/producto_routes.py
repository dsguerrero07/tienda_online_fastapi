from fastapi import APIRouter

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def listar_productos():
    return {"mensaje": "Aquí se listarán los productos"}
