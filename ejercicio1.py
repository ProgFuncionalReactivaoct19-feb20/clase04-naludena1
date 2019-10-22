"""
	@naludena1
"""

listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]


listaB1 = sorted(listaB, reverse = True)
listaA1 = sorted(listaA)

listaFinal = (list(zip(listaA1, listaB1)))
print(listaFinal)
print(max(listaFinal))