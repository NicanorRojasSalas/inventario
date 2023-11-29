from fastapi import APIRouter, Depends,  HTTPException, status
from sqlalchemy.orm import Session

from api.config.datos import get_conexion

from comun.esquemas import EscribirInvntr
from api.core.invntr.operaciones import *

routerInvntr = APIRouter(prefix="/inventario", tags=["Inventario",] )


@routerInvntr.post("/",
                 name="Agregar Inventario",
                 description="Permite agregar un nuevo inventario",
                 status_code= status.HTTP_201_CREATED
                )
def crear_invntr( Inventario : EscribirInvntr, conexion : Session = Depends(get_conexion)):
    return insertar_invntr(conn = conexion, prdct=Inventario) 


@routerInvntr.put("/{Id:int}",
                 name="Editar Inventario",
                 description ="Permite editar un inventario existente",
                 status_code = status.HTTP_202_ACCEPTED
               )
def editar_invntr( Id : int, Inventario : EscribirInvntr, conexion : Session = Depends(get_conexion)):
    db_invntr = obtener_invntr(conn = conexion, id = Id)
    if db_invntr is None:
        raise HTTPException(status_code=400, detail="Inventario no encontrado")
    return actualizar_invntr(conn = conexion, id = Id, invntr = Inventario)


@routerInvntr.delete("/{Id:int}",
                    name="Eliminar Inventario",
                    description="Permite eliminar un inventario",
                    status_code= status.HTTP_202_ACCEPTED
                   )
def borrar_invntr(Id : int, conexion : Session = Depends(get_conexion)):
    db_invntr = obtener_invntr(conn = conexion, Id = Id)
    if db_invntr is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return eliminar_invntr(conn = conexion, id=Id)


@routerInvntr.get("/",
                name="Obtener Inventario",
                description="Permite obtener una lista de inventario",
                status_code= status.HTTP_202_ACCEPTED               
               )
def leer_invntr(Skip : int = 0, Limit : int = 100, conexion : Session = Depends(get_conexion)):
    inventario = obtener_invntr(conn=conexion, skip=Skip, limit=Limit)
    return inventario


@routerInvntr.get("/{Id:int}",
                name="Obtener Inventario por Id",
                description="Permite obtener la info de un inventario",
                status_code= status.HTTP_202_ACCEPTED
               )
def leer_invntr( Id : int, conexion : Session = Depends(get_conexion)):
    db_invntr = obtener_invntr(conn = conexion, id = Id)
    if db_invntr is None:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return db_invntr
