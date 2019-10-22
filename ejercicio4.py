"""
	@naludena1
	Manejo de colecciones y Tuplas
"""
# Encontrar la siguiente estructura
#
# [(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
#


paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

suma0 = lambda x: x[0]
suma1 = lambda x: x[1]
suma2 = lambda x: x[2]

resultado = lambda x: ((suma0(x) + suma1(x) + suma2(x))/3) 
resultado1= (list(map(resultado, paraleloA)))

# Presentar el resultado en una lista
print(list(zip(resultado1, nombres)))

