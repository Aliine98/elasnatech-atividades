def get_imc(altura, peso):
    imc = peso / (altura ** 2)
    msg = ''
    if imc <= 18.5:
        msg = 'Abaixo do peso'
    elif 18.6 <= imc <= 24.9:
        msg = 'Peso ideal'
    elif 25 <= imc <= 29.9:
        msg = 'Levemente acima do peso'
    elif 30 <= imc <= 34.9:
        msg = 'Obesidade grau I'
    elif 35 <= imc <= 39.9:
        msg = 'Obesidade grau II (Severa)'
    else:
        msg = 'Obesidade grau III (Grave)'
    return msg
    return f'Seu imc é {imc:.2f} \n{msg}'

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso em kg: '))
print(get_imc(altura, peso))