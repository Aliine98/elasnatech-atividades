try:
    valor = int(input('digite o valor do seu produto: '))
    print(valor * 0.5)
except ValueError:
    print('digite apenas números')
else:
    print('código ok')
finally:
    print('executando com erro ou sem erro')


print('mais código mesmo com erro acima')