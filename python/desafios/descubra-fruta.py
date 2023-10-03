fruta = input('Qual a fruta? ').lower()
while fruta != 'abacate':
    print('Tente novamente')
    fruta = input('Qual a fruta? ').lower()
    if fruta == 'abacate':
        print('Parabéns, você acertou a fruta!')
