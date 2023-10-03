frutas = ['maçã', 'banana', 'maçã', 'morango', 'maçã', 'maracujá']

qtd_maca = frutas.count('maçã')
print(f'Há {qtd_maca} maçãs na lista')

qtd_maca = 0
for fruta in frutas:
    if fruta == 'maçã':
        qtd_maca += 1

print(f'Há {qtd_maca} maçãs na lista')
