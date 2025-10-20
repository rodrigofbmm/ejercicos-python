from fastapi import FastAPI, HTTPException
from schemas import (
    AnimalEntrada, AnimalSalida, VeterinarioEntrada, VeterinarioSalida, VisitaEntrada, DiagnosticoSalida
)

from funciones import (
    registrar_veterinario, listar_veterinarios, registrar_animal, atender
)

app = FastAPI(title="Veterinaria API: Animales + Diagnóstico")

@app.post("/veterinarios", response_model=VeterinarioSalida)
def crear_veterinario(body: VeterinarioEntrada):
    registrar_veterinario(body.nombre, body.registro)
    return listar_veterinarios()[-1]

@app.get("/veterinarios", response_model=list[VeterinarioSalida])
def get_veterinarios():
    return listar_veterinarios()

@app.post("/animales", response_model=AnimalSalida)
def crear_animal(body: AnimalEntrada):
    return registrar_animal(body)

@app.post("/veterinarios/{nombre}/atender", response_model=DiagnosticoSalida)
def post_atender(nombre: str, body: VisitaEntrada):
    try:
        return atender(nombre, body)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
