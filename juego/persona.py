class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años\n")


def crear_persona():
    nombre = input("Introduce tu nombre: ")
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            break
        except ValueError:
            print("introduce un número válido para la edad.")

    persona = Persona(nombre, edad)
    print("Persona creada correctamente.")
    persona.mostrar_info()
    return persona
