"""
	@naludena1
	Manejo de colecciones y Tuplas
"""
# Encontrar la siguiente estructura
#
#[((20, 4), 'c'), ((30, 1), 'B'), ((100, 2), 'A')]
#

lista = [(100, 2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]

lista_1 = sorted(lista)
lista_2 = map(lambda x: x.upper(), lista2)

print(list(zip(lista_1, sorted(lista_2, reverse = True))))

