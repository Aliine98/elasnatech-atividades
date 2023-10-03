idade = int(input('Qual a sua idade? '))

if idade < 13:
    print('Você é uma criança')
elif idade >= 13 and idade < 20:
    print('Você é um adolescente')
else:
    print('Você é um adulto')
