from pydantic import BaseModel, Field

class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50, description="Nombre de la categoría")
    descripcion: str | None = Field(None, max_length=200)

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    activa: bool | None = True

class CategoriaOut(CategoriaBase):
    id: int
    activa: bool

    class Config:
        orm_mode = True
