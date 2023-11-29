from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, SecretStr, Field


class LeerPrdct(BaseModel):
    
    id : int = Field(title="Id Producto")
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo para el producto", max_length=20)
    nmbr : str = Field(alias="Nombre", title="Nombre", description="Nombre para el producto", max_length=100)
    dscr : str = Field(alias="Descripcion", title="Descripcion", description="Descripcion para el producto", max_length=200)
    prsn : str = Field(alias="Presentacion", title="Presentacion", description="Presentacion para el producto", max_length=50)
    crdo : datetime = Field(alias="Creado el", title="Creado el", description="Fecha de creacion del producto")
    actv : bool = Field(alias="Activo", title="Activo ?", description="Productio activo ?")
    
    class Config:
        from_attributes = True
    
    
class EscribirPrdct(BaseModel):
    
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo para el producto", max_length=20)
    nmbr : str = Field(alias="Nombre", title="Nombre", description="Nombre para el producto", max_length=100)
    dscr : str = Field(alias="Descripcion", title="Descripcion", description="Descripcion para el producto", max_length=200)
    prsn : str = Field(alias="Presentacion", title="Presentacion", description="Presentacion para el producto", max_length=50)
           
    class Config:
        from_attributes = True


class LeerInvntr(BaseModel):
    
    id : int = Field(title="Id Usuario")
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo para el producto", max_length=20)
    prdct_id : int = Field(title="Id Producto")
    cmpr : datetime = Field(alias="Fecha Compra", title="Fecha Compra", description="Fecha Compra")
    vnce : datetime = Field(alias="Fecha Vencimiento", title="Vencimiento", description="Fecha vencimiento del producto")
    inic : int = Field(alias="Cantidad", title="Cantidad", description="Cantidad de productos")
    actu : int = Field(alias="Disponible", title="Disponible", description="Productos disponibles")
    vlor : int = Field(alias="Valor", title="Valor",description="Valor del producto")
    crdo : datetime = Field(alias="Creado el", title="Creado el", description="Fecha de creacion del producto")
    actv : bool = Field(alias="Activo", title="Activo ?", description="Productio activo ?")
    
    class Config:
        from_attributes = True
    
    
class EscribirInvntr(BaseModel):
    
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo para el usuario", max_length=20)
    prdct_id : int = Field(title="Id Producto")
    cmpr : datetime = Field(alias="Fecha Compra", title="Fecha Compra", description="Fecha Compra")
    vnce : datetime = Field(alias="Fecha Vencimiento", title="Vencimiento", description="Fecha vencimiento del producto")
    inic : int = Field(alias="Cantidad", title="Cantidad", description="Cantidad de productos")
    actu : int = Field(alias="Disponible", title="Disponible", description="Productos disponibles")
    vlor : int = Field(alias="Valor", title="Valor",description="Valor del producto")
           
    class Config:
        from_attributes = True
        
        
class LeerDtllVnta(BaseModel):
    
    id : int = Field(title="Id Detalle Venta")
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo Detalle Venta", max_length=20)
    cntd  : int = Field(alias="Cantidad", title="Cantidad", description="Cantidad")
    vlor : int = Field(alias="Valor", title="Valor",description="Valor")
    
    invntr_id : int = Field(title="Id Inventario")
    vnta_id : int = Field(title="Id Venta")
    
    
    class Config:
        from_attributes = True
    
    
class EscribirDtllVnta(BaseModel):
    
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo Detalle Venta", max_length=20)
    cntd  : int = Field(alias="Cantidad", title="Cantidad", description="Cantidad")
    vlor : int = Field(alias="Valor", title="Valor",description="Valor")
    invntr_id : int = Field(title="Id Inventario")
    vnta_id : int = Field(title="Id Venta")           
    
    class Config:
        from_attributes = True


class LeerVnta(BaseModel):
    
    id : int = Field(title="Id Venta")
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo para la venta", max_length=20)
    fcha : datetime = Field(alias="Fecha", title="Fecha", description="Fecha de Compra")
    cmprdr : str = Field(alias="Comprador", title="Comprador",description="Comprador", max_length=100)
    tlfn : str = Field(alias="Telefono", title="Telefono",description="Telefono", max_length=20) 
    
    class Config:
        from_attributes = True
    
    
class EscribirVnta(BaseModel):
    
    cdgo : str = Field(alias="Codigo", title="Codigo",description="Codigo para la Venta", max_length=20)
    fcha : datetime = Field(alias="Fecha", title="Fecha", description="Fecha de Compra")
    cmprdr : str = Field(alias="Comprador", title="Comprador",description="Comprador", max_length=100)
    tlfn : str = Field(alias="Telefono", title="Telefono",description="Telefono", max_length=20) 
           
    class Config:
        from_attributes = True


