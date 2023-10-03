frutas = ['maçã', 'banana', 'manga', 'uva']
print(frutas)
print(f'Primeira fruta: {frutas[0]}')
print(f'Última fruta: {frutas[-1]}')

frutas[1] = 'morango'
frutas.append('abacaxi')
print(frutas)
frutas.remove('manga')
del frutas[-1]
print(frutas)

for fruta in frutas:
    print(f'Eu gosto de {fruta}')
