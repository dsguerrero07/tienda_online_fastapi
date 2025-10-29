from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    stock: int
    descripcion: str
    activo: bool = Field(default=True)

    categoria_id: int = Field(foreign_key="categoria.id")
    categoria: Optional["Categoria"] = Relationship(back_populates="productos")
