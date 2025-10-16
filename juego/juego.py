import random

def jugar():
    numero_secreto = random.randint(1, 10)
    vidas = 3

    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes 3 vidas para adivinar un número entre 1 y 10.\n")

    while vidas > 0:
        try:
            intento = int(input("Adivina el número: "))
            if intento < 1 or intento > 10:
                print("Debes elegir un número entre 1 y 10.")
                continue

            if intento == numero_secreto:
                print("¡Correcto! Adivinaste el número.")
                break
            else:
                print("Prueba otro número.")
                vidas -= 1

                if vidas > 0:
                    print(f"Te quedan {vidas} vidas.\n")
                else:
                    print(f"Adios. El número era {numero_secreto}.")
        except ValueError:
            print("Introduce un número válido.\n")
