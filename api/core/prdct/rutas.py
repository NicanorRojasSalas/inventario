from fastapi import APIRouter, Depends,  HTTPException, status
from sqlalchemy.orm import Session

from api.config.datos import get_conexion

from comun.esquemas import EscribirPrdct
from api.core.prdct.operaciones import *

routerPrdct = APIRouter(prefix="/productos", tags=["Productos",] )


@routerPrdct.post("/",
                 name="Agregar Producto",
                 description="Permite agregar un nuevo producto",
                 status_code= status.HTTP_201_CREATED
                )
def crear_prdct( Producto : EscribirPrdct, conexion : Session = Depends(get_conexion)):
    return insertar_prdct(conn = conexion, prdct=Producto) 


@routerPrdct.put("/{Id:int}",
                 name="Editar Producto",
                 description ="Permite editar un producto existente",
                 status_code = status.HTTP_202_ACCEPTED
               )
def editar_prdct( Id : int, Producto : EscribirPrdct, conexion : Session = Depends(get_conexion)):
    db_prdct = obtener_prdct(conn = conexion, id = Id)
    if db_prdct is None:
        raise HTTPException(status_code=400, detail="Producto no encontrado")
    return actualizar_prdct(conn = conexion, id = Id, prdct = Producto)


@routerPrdct.delete("/{Id:int}",
                    name="Eliminar Producto",
                    description="Permite eliminar un producto",
                    status_code= status.HTTP_202_ACCEPTED
                   )
def borrar_prdct(Id : int, conexion : Session = Depends(get_conexion)):
    db_prdct = obtener_prdct(conn = conexion, Id = Id)
    if db_prdct is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return eliminar_prdct(conn = conexion, id=Id)


@routerPrdct.get("/",
                name="Obtener Productos",
                description="Permite obtener una lista de productos",
                status_code= status.HTTP_202_ACCEPTED               
               )
def leer_prdcts(Skip : int = 0, Limit : int = 100, conexion : Session = Depends(get_conexion)):
    productos = obtener_prdcts(conn=conexion, skip=Skip, limit=Limit)
    return productos


@routerPrdct.get("/{Id:int}",
                name="Obtener Producto por Id",
                description="Permite obtener la info de un producto",
                status_code= status.HTTP_202_ACCEPTED
               )
def leer_prdct( Id : int, conexion : Session = Depends(get_conexion)):
    db_prdct = obtener_prdct(conn = conexion, id = Id)
    if db_prdct is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_prdct

