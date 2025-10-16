import random

def jugar(jugador):
    numero_secreto = random.randint(1, 10)
    vidas = 3
    print(f"\n¡Bienvenido, {jugador.nombre}! Adivina el número entre 1 y 10.")
    print(f"Tienes {vidas} vidas.\n")

    while vidas > 0:
        try:
            intento = int(input("Adivina el número: "))
            if intento < 1 or intento > 10:
                print("Debes elegir un número entre 1 y 10.")
                continue
            if intento == numero_secreto:
                print("¡Correcto! Adivinaste el número.")
                jugador.actualizar_estadisticas(True)
                return
            else:
                print("Prueba otro número.")
                vidas -= 1
                if vidas > 0:
                    print(f"Te quedan {vidas} vidas.\n")
                else:
                    print(f"Adiós. El número era {numero_secreto}.")
                    jugador.actualizar_estadisticas(False)
                    return
        except ValueError:
            print("Introduce un número válido.\n")
