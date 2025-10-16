class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.partidas_jugadas = 0
        self.aciertos = 0

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Partidas jugadas: {self.partidas_jugadas}")
        print(f"Acertos: {self.aciertos}\n")

    def actualizar_estadisticas(self, acerto):
        self.partidas_jugadas += 1
        if acerto:
            self.aciertos += 1

def crear_persona():
    nombre = input("Introduce tu nombre: ")
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            break
        except ValueError:
            print("Introduce un número válido para la edad.")
    return Persona(nombre, edad)

