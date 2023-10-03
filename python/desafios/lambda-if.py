verifica_num = lambda n: 'par' if n % 2 == 0 else 'impar'

num = int(input('Digite um número: '))
print(f'O número {num} é {verifica_num(num)}')