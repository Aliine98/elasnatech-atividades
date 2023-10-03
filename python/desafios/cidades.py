set = {'são paulo', 'rio de janeiro', 'belo horizonte'}
tuple = ('são paulo', 'rio de janeiro', 'belo horizonte')
user_search = input('Digite uma cidade: ').lower()

if user_search in set:
    print('Cidade encontrada')
else:
    print('Cidade não encontrada')

if user_search in tuple:
    print('Cidade encontrada')
else:
    print('Cidade não encontrada')
