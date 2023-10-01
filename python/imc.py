def get_imc(altura, peso):
    imc = peso / (altura ** 2)
    msg = ''
    if imc < 18.5:
        msg = 'Abaixo do peso'
    elif imc < 25:
        msg = 'Peso ideal'
    elif imc < 30:
        msg = 'Sobrepeso'
    elif imc < 40:
        msg = 'Obesidade'
    else:
        msg = 'Obesidade grave'
    return f'Seu imc é {imc:.2f} \n{msg}'

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso em kg: '))
print(get_imc(altura, peso))