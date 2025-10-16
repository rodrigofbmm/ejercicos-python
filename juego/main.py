from persona import crear_persona, Persona
from juego import jugar

def menu():
    jugador = None
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear una persona")
        print("2. Jugar al juego de adivinar el número")
        print("3. Ver estadísticas")
        print("4. Eliminar persona")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugador = crear_persona()
        elif opcion == "2":
            if jugador:
                jugar(jugador)
            else:
                print("Primero debes crear una persona.")
        elif opcion == "3":
            if jugador:
                jugador.mostrar_info()
            else:
                print("Primero debes crear una persona.")
        elif opcion == "4":

            print("No hay ninguna persona creada para eliminar.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
