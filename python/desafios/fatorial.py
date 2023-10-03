def fatorial(n):
    if n > 1:
        return n * fatorial(n - 1)
    else:
        return 1


num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {fatorial(num)}')
