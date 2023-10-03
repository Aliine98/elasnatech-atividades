cars = ['BMW X6', 'BMW i5', 'BMW i8']

user_wanted_car = input('Selecione o modelo do carro que deseja comprar: ')

if user_wanted_car in cars:
    print('Este carro está disponível')
else:
    print('Desculpe, este carro não está disponível')
