"""
	@naludena1
	Manejo de colecciones y Tuplas
"""
# Encontrar la siguiente estructura
#
# [("a", (30, 1)), ("b", (100, 2)), ("c", (20, 4))]
#

lista1 = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

"""
lista_1 = sorted(lista1, key = lambda x: x[1])
lista_2 = sorted(lista2)

print(list(zip(lista_2, lista_1)))
"""


print(list(zip(sorted(lista2), sorted(lista1, key = lambda x: x[1]))))