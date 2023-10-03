paises_capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Itália': 'Roma'
}

pais = input('Digite um país: ')

if pais in paises_capitais.keys():
    print(f'A capital de {pais} é {paises_capitais[pais]}')
else:
    print('Desculpe, não temos informações sobre a capital deste país.')
