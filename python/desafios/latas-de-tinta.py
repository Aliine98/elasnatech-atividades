def calc_latas_tinta(rendimento, altura, largura):
    area = altura * largura
    total_latas = area / rendimento
    print(f'Você precisa de {total_latas} latas de tinta')


rendimento = int(input('Informe o rendimento da lata de tinta:'))
altura = int(input('Informe a altura da parede:'))
largura = int(input('Informe a largura da parede:'))

calc_latas_tinta(rendimento, altura, largura)
