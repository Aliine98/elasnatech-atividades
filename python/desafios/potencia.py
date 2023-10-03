def potencia(base, expoente=2):
    return base ** expoente


print(potencia(2, 3))
print(potencia(2))

base = int(input('Digite a base: '))
expoente = input('Digite o expoente: ')
if expoente:
    print(potencia(base, int(expoente)))
else:
    print(potencia(base))
