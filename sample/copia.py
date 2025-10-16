import copy

empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

for e in empleados:
    print(e)

empleados_copia = copy.deepcopy(empleados)
print("¿Misma referencia?", empleados is empleados_copia)  
empleados_copia[-1][1].append("Java")
nuevo_empleado = ["Juan", ["Node.js", "redis"]]
empleados_copia.append(nuevo_empleado)

print("\nLista Deep Copy final:")
for e in empleados_copia:
    print(e)
    

