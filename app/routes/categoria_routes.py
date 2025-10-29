from fastapi import APIRouter

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/")
def listar_categorias():
    return {"mensaje": "Aquí se listarán las categorías"}
