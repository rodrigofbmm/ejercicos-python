from persona import crear_persona
from juego import jugar

def menu():
    persona_creada = None

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear una persona")
        print("2. Jugar al juego de adivinar el número")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            persona_creada = crear_persona()
        elif opcion == "2":
            if persona_creada:
                print(f"Hola {persona_creada.nombre}, ¡vamos a jugar!")
            else:
                print("Primero debes crear una persona.")
                continue
            jugar()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
