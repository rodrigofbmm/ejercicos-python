import random
import threading

def jugar(jugador, dificultad):
    config = {"facil": (5, 10), "dificil": (2, 5)}
    vidas, tiempo = config[dificultad]
    secreto = random.randint(1, 10)
    print(f"\n{jugador.nombre}, adivina un número entre 1 y 10. Vidas: {vidas}")

    while vidas > 0:
        intento = [None]
        agotado = [False]

        def leer():
            try:
                intento[0] = int(input(f"Adivina ({tiempo}s): "))
            except:
                intento[0] = -1

        t = threading.Timer(tiempo, lambda: agotado.__setitem__(0, True))
        t.start()
        hilo = threading.Thread(target=leer)
        hilo.start()
        hilo.join(timeout=tiempo)
        t.cancel()

        if agotado[0]:
            print("¡Tiempo agotado!")
        elif intento[0] == secreto:
            print("¡Correcto!")
            jugador.actualizar_estadisticas(True, dificultad)
            return
        elif intento[0] not in range(1, 11):
            print("Número entre 1 y 10.")
        else:
            print("Incorrecto.")

        vidas -= 1
        print(f"Vidas restantes: {vidas}" if vidas > 0 else f"Fin. Número era {secreto}")
        if vidas == 0:
            jugador.actualizar_estadisticas(False, dificultad)
