from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, unique=True)
    descripcion: str
    activa: bool = Field(default=True)
    
    productos: List["Producto"] = Relationship(back_populates="categoria")
