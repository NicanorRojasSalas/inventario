from datetime import datetime
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, DateTime, Boolean, Integer
from sqlalchemy.orm import Mapped , mapped_column , relationship, declared_attr

from api.config.datos import modeloBase 

 
# Productos
class Prdct(modeloBase):
    
    __tablename__ = "prdcts"
    
    id  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True) # Id 
    cdgo : Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False) # Codigo
    nmbr : Mapped[str] = mapped_column(String(100), index=True, nullable=False) # Nombre
    dscr : Mapped[str] = mapped_column(String(200), index=True, nullable=False)  # Descripcion
    prsn : Mapped[str] = mapped_column(String(50), index=True, nullable=False)  # Presentacion   
    crdo : Mapped[datetime] = mapped_column(DateTime, insert_default=datetime.now)
    actv : Mapped[bool] = mapped_column(Boolean, default=True)
    
    invntrs   : Mapped[List["Invntr"]] = relationship(back_populates="prdct")
   
      
    def __repr__(self) -> str:
        return f"Producto : (id={self.id!r}, nombre={self.nmbr!r}, presentacion={self.prsn})"
    

 
# Inventario
class Invntr(modeloBase):
    
    __tablename__ = "invntrs"
   
    id  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)  
    cdgo : Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False) # Codigo
    cmpr : Mapped[datetime] = mapped_column(DateTime, nullable=False)
    vnce : Mapped[datetime] = mapped_column(DateTime, nullable=False)
    inic : Mapped[int] = mapped_column(Integer)  
    actu : Mapped[int] = mapped_column(Integer)  
    vlor : Mapped[int] = mapped_column(Integer)
    crdo : Mapped[datetime] = mapped_column(DateTime, insert_default=datetime.now)
    actv : Mapped[bool] = mapped_column(Boolean, default=True)
    
    prdct_id : Mapped[int] = mapped_column(ForeignKey("prdcts.id"))
    prdct    : Mapped["Prdct"] = relationship(back_populates="invntrs")
    
    dtllVnta : Mapped["DtllVnta"] = relationship(back_populates="invntr")
    
    
    
           
    def __repr__(self) -> str:
        return f"Inventario : (id={self.id!r}, Producto = {self.prdct.nmbr!r}, Disponible={self.actu})"
    
    

# Venta
class Vnta(modeloBase):
    
    __tablename__ = "vntas"
   
    id  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True) 
    cdgo : Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False) # Codigo 
    fcha : Mapped[datetime] = mapped_column(DateTime, nullable=False)
    cmprdr : Mapped[str] = mapped_column(String(100), index=True, nullable=False) # Comprador
    tlfn : Mapped[str] = mapped_column(String(20), index=True, nullable=False) # Telefono
    
    dtllVnta : Mapped[List["DtllVnta"]] = relationship(back_populates="vnta")
           
    def __repr__(self) -> str:
        return f"Inventario : (id={self.id!r}"
    

#DetalleVenta
class DtllVnta(modeloBase):
    
    __tablename__ = "dtllsVntas"
   
    id  : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True) 
    cdgo : Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False) # Codigo 
   
    invntr_id : Mapped[int] = mapped_column(ForeignKey("invntrs.id"))
    invntr : Mapped["Invntr"] = relationship(back_populates="dtllVnta")
    
    cntd : Mapped[int] = mapped_column(Integer)  # cantidad comprada
    vlor : Mapped[int] = mapped_column(Integer)  # valor unitario
     
    vnta_id : Mapped[int] = mapped_column(ForeignKey("vntas.id"))
    vnta : Mapped["Vnta"] = relationship(back_populates="dtllVnta")
    
    def __repr__(self) -> str:
        return f"Detalle Venta : (id={self.id!r}"
    
    
    
    
    
