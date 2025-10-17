from persona import crear_persona, seleccionar_jugador
from juego import jugar

def menu():
    jugadores = []
    while True:
        print("\n1. Crear jugador")
        print("2. Jugar")
        print("3. Estadísticas jugador ")
        print("4. Eliminar jugador")
        print("5. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            jugadores.append(crear_persona())
        elif opcion == "2":
            j = seleccionar_jugador(jugadores)
            if j:
                dif = "facil" if input("1. Fácil 2. Difícil: ") == "1" else "dificil"
                jugar(j, dif)
        elif opcion == "3":
            j = seleccionar_jugador(jugadores, "Ver estadísticas de: ")
            if j: j.mostrar_info()
        elif opcion == "4":
            j = seleccionar_jugador(jugadores, "Eliminar jugador: ")
            if j:
                jugadores.remove(j)
                print(f"{j.nombre} eliminado")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
