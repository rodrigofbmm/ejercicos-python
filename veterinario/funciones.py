from clases import Perro, Gato, Veterinario
from schemas import AnimalEntrada, AnimalSalida, VisitaEntrada, DiagnosticoSalida

veterinarios = []
animales = []

def registrar_veterinario(nombre: str, registro: str):
    vet = Veterinario(nombre, registro)
    veterinarios.append(vet)
    return vet

def listar_veterinarios():
    return veterinarios

def registrar_animal(body: AnimalEntrada) -> AnimalSalida:
    if body.tipo == "perro":
        animal = Perro(body.nombre, body.edad)
    else:
        animal = Gato(body.nombre, body.edad)
    animales.append(animal)
    return AnimalSalida(nombre=animal.nombre, edad=animal.edad, tipo=body.tipo, sonido=animal.sonido())

def atender(nombre: str, body: VisitaEntrada) -> DiagnosticoSalida:
    vet = next((v for v in veterinarios if v.nombre == nombre), None)
    if not vet:
        raise ValueError("Veterinario no encontrado")

    animal = Perro(body.nombre, body.edad) if body.tipo == "perro" else Gato(body.nombre, body.edad)
    mensaje = vet.atender(animal)
    return DiagnosticoSalida(mensaje=mensaje)
