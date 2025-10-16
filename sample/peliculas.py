peliculas = {}

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Añadir película")
    print("2. Eliminar película")
    print("3. Mostrar películas")
    print("4. Buscar película")
    print("5. Modificar datos de película")
    print("6. Eliminar todas las películas")
    print("7. Salir")

def añadir_pelicula():
    nombre = input("nombre de la película: ")
    if nombre in peliculas:
        print(f"'{nombre}' ya existe.")
        return
    director = input("director: ")
    año = input("año: ")
    presupuesto = input("presupuesto: ")
    peliculas[nombre] = {
        "director": director,
        "año": año,
        "presupuesto": presupuesto
    }
    print(f"'{nombre}' añadida.")

def eliminar_pelicula():
    nombre = input("Introduce el nombre de la película a eliminar: ")
    if nombre in peliculas:
        del peliculas[nombre]
        print(f"'{nombre}' eliminada correctamente.")
    else:
        print(f"'{nombre}' no encontrada en la lista.")

def mostrar_peliculas():
    if not peliculas:
        print("La lista está vacía.")
    else:
        print("Lista de películas:")
        for nombre, datos in peliculas.items():
            print(f"- {nombre}: Director: {datos['director']}, Año: {datos['año']}, Presupuesto: {datos['presupuesto']}")

def buscar_pelicula():
    nombre = input("Introduce el nombre de la película a buscar: ")
    if nombre in peliculas:
        datos = peliculas[nombre]
        print(f"'{nombre}' está en la lista. Director: {datos['director']}, Año: {datos['año']}, Presupuesto: {datos['presupuesto']}")
    else:
        print(f"'{nombre}' no encontrada en la lista.")

def modificar_pelicula():
    nombre = input("Introduce el nombre de la película a modificar: ")
    if nombre in peliculas:
        print(f"Modificando '{nombre}':")
        director = input(f"Director actual: {peliculas[nombre]['director']}. Nuevo director (dejar en blanco para no cambiar): ")
        año = input(f"Año actual: {peliculas[nombre]['año']}. Nuevo año (dejar en blanco para no cambiar): ")
        presupuesto = input(f"Presupuesto actual: {peliculas[nombre]['presupuesto']}. Nuevo presupuesto (dejar en blanco para no cambiar): ")

        if director:
            peliculas[nombre]['director'] = director
        if año:
            peliculas[nombre]['año'] = año
        if presupuesto:
            peliculas[nombre]['presupuesto'] = presupuesto

        print(f"'{nombre}' modificada correctamente.")
    else:
        print(f"'{nombre}' no encontrada en la lista.")

def eliminar_todas():
    peliculas.clear()
    print("Todas las películas han sido eliminadas.")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-7): ")
    if opcion == "1":
        añadir_pelicula()
    elif opcion == "2":
        eliminar_pelicula()
    elif opcion == "3":
        mostrar_peliculas()
    elif opcion == "4":
        buscar_pelicula()
    elif opcion == "5":
        modificar_pelicula()
    elif opcion == "6":
        eliminar_todas()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
