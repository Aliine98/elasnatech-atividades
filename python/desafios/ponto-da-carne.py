temperatura = int(input('Informa a temperatura em celsius:'))

if temperatura < 48:
    print('Ainda está cru! Cozinhe mais')
# elif 53 >= temperatura >= 48:
#     print('Selada')
# elif 59 >= temperatura >= 54:
#     print('Mal passada')
# elif 64 >= temperatura >= 60:
#     print('Ao ponto')
# elif 70 >= temperatura >= 65:
#     print('Ao ponto para bem passada')
elif temperatura in range(48, 54):
    print('Selada')
elif temperatura in range(54, 60):
    print('Mal passada')
elif temperatura in range(60, 65):
    print('Ao ponto')
elif temperatura in range(65, 71):
    print('Ao ponto para bem passada')
elif temperatura in range(71, 81):
    print('Bem passada')
else:
    print('Já queimou')
