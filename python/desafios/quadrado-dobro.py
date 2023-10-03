def dobro(n):
    return n * 2

def quadrado(n):
    return dobro(n) ** 2

num = int(input('Digite um número: '))
print(f'O quadrado do dobro de {num} é {quadrado(num)}')