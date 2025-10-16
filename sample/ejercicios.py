
texto_largo = ["Línea " + str(i + 1) for i in range(1000)]

bloques = []
bloque_actual = []

for linea in texto_largo:
    bloque_actual.append(linea)

    if len(bloque_actual) == 25:
        bloques.append(bloque_actual)
        bloque_actual = []

print("Número total de bloques:", len(bloques))
print("Ejemplo del primer bloque:", bloques[0])



print("------------------")
print("ej 1")

from decimal import Decimal, getcontext

getcontext().prec = 5

precio_base = Decimal("120.0") 
iva_porcentaje = Decimal("21")

precio_iva = precio_base * iva_porcentaje / Decimal("100")
precio_final = precio_base + precio_iva


mensaje = f"El precio final es {precio_final} , IVA {precio_iva}"

assert precio_iva == Decimal("25.2")
assert precio_final == Decimal("145.2")
assert mensaje == f"El precio final es 145.2 , IVA 25.2"

print(mensaje)


"""ejercicio 2"""

print("------------------")w
print("ej 2")

nombre_completo = "  ana  MARÍA  lopez  "

nombre_normalizado = " ".join(nombre_completo.split()).title()

iniciales = ".".join([nombre[0].upper() for nombre in nombre_normalizado.split()])

print("Nombre normalizado:", nombre_normalizado)
print("Iniciales:", iniciales)


"""ejercicio 3"""

print("------------------")
print("ej 3")

inicio, fin = 1, 10
pares, impares = 0, 0

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Entre {inicio} y {fin} hay {pares} números pares y {impares} impares.")

"""ejercicio 4"""

print("------------------")
print("ej 4")

from typing import Iterable, Tuple

def estadisticas(valores: Iterable[float]) -> Tuple[float, float, float]:
    if not valores:
        raise ValueError("Vacío")
    v = list(valores)
    return min(v), max(v), sum(v) / len(v)

# Ejemplo
print(estadisticas([4, 8, 15, 16, 23, 42]))

