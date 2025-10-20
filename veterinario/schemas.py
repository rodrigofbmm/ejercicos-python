from pydantic import BaseModel, Field
from typing import Literal

# Entrada de animal
class AnimalEntrada(BaseModel):
    tipo: Literal["perro", "gato"]
    nombre: str
    edad: int = Field(ge=0)

class AnimalSalida(BaseModel):
    nombre: str
    edad: int
    tipo: str
    sonido: str

class VeterinarioEntrada(BaseModel):
    nombre: str
    registro: str

class VeterinarioSalida(BaseModel):
    nombre: str
    registro: str

class VisitaEntrada(BaseModel):
    tipo: Literal["perro", "gato"]
    nombre: str
    edad: int

class DiagnosticoSalida(BaseModel):
    mensaje: str
