quadrado = lambda n: n * 2

numeros = [1, 2, 3, 4, 5]

numeros_quadrados = [quadrado(n) for n in numeros]
numeros_quadrados2 = list(map(quadrado, numeros))

print(numeros_quadrados)
print(numeros_quadrados2)