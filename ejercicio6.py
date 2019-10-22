"""
	@naludena1
	Manejo de colecciones y Tuplas
"""
# Encontrar la siguiente estructura
#
# [(4.333333333333333, 13, 'Ángel'), (4.666666666666667, 14, 'Ana')]
#

paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]


# Obtrncion del promedio
promedio = list(map(lambda x: sum(x) / len(x), paraleloA))

# Suma de las tuplas y uso de funciones
suma = list(map(lambda	x: sum(x), paraleloA))


# Uso del zip para la union
resultado1 = list(zip(promedio, suma, nombres))

# Presentar resultados y condicional
print(list(filter(lambda x: x[0] <= 5, resultado1)))



