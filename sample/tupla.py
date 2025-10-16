tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})
print("Tupla original:", tupla_mixta)

lista_mixta = list(tupla_mixta)
print("\nLista convertida:", lista_mixta)

lista_mixta[1] = "DOS"
print("\nLista modificada:", lista_mixta)

tupla_mixta = tuple(lista_mixta)
print("\nTupla convertida de nuevo:", tupla_mixta)

print("\nElemento [1] de la tupla:", tupla_mixta[1])

tupla_numerica = (10, 20, 30, 40, 50)
print("\nTupla numérica:", tupla_numerica)

print("Suma:", sum(tupla_numerica))
print("Máximo:", max(tupla_numerica))
print("Mínimo:", min(tupla_numerica))

cuadrados = tuple(x**2 for x in tupla_numerica)
print("\nCuadrados de la tupla:", cuadrados)

a, b, c, d, e = tupla_numerica
print(f"\nValores desempaquetados: a={a}, b={b}, c={c}, d={d}, e={e}")
