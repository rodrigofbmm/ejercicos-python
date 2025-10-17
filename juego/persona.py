class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.stats = {
            "facil": {"partidas":0,"aciertos":0}, 
            "dificil": {"partidas":0,"aciertos":0}
            }

    def mostrar_info(self):
        print(f"{self.nombre} ({self.edad} años)")
        for nivel, datos in self.stats.items():
            print(f"{nivel.capitalize()}: jugados -> {datos['aciertos']}/{datos['partidas']} <-aciertos")

    def actualizar_estadisticas(self, acerto, dificultad):
        self.stats[dificultad]["partidas"] += 1
        if acerto:
            self.stats[dificultad]["aciertos"] += 1

def crear_persona():
    nombre = input("Nombre: ")
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Introduce un número válido.")
    return Persona(nombre, edad)

def seleccionar_jugador(jugadores, msg="Selecciona jugador: "):
    if not jugadores: 
        print("No hay jugadores.")
        return None
    for i, j in enumerate(jugadores, 1):
        print(f"{i}. {j.nombre} ({j.edad})")
    try:
        idx = int(input(msg)) - 1
        return jugadores[idx] if 0 <= idx < len(jugadores) else None
    except:
        return None
