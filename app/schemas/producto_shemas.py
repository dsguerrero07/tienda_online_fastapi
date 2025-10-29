from pydantic import BaseModel, Field, PositiveFloat, PositiveInt

class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: str | None = Field(None, max_length=250)
    precio: PositiveFloat = Field(..., description="Debe ser un valor positivo")
    stock: PositiveInt = Field(..., description="Debe ser un número entero positivo")
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    activo: bool | None = True

class ProductoOut(ProductoBase):
    id: int
    activo: bool

    class Config:
        orm_mode = True
