import os

from pathlib import Path

ruta_archivo = Path.cwd() / "demo_generadores.txt"

def generar_lineas_iniciales():
    for i in range(1, 4):
        yield f"Líneas iniciales {i}\n"
        
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    for linea in generar_lineas_iniciales():
        archivo.write(linea)
        
print(f"Archivo creado en: { ruta_archivo}")    

def generar_lineas_adicionales():
    for i in range(4, 7):
        yield f"Línea adicional {i}\n"
        
with open(ruta_archivo, "a", encoding="utf-8") as archivo:
    for linea in generar_lineas_adicionales():
        archivo.write(linea)

def leer_y_procesar(path: Path):
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            yield linea.strip().upper()

print("Este es el contenido del archivo procesado")
for linea in leer_y_procesar(ruta_archivo):
    print(linea)