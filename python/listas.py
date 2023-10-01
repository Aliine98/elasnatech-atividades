from sys import getsizeof

#juntando listas pelo index
lista1 = ['maça', 'banana','morango','maracujá']
lista2 = [0,1,2,3]

#zip transforma listas em tuples para cada index
listas_juntas = list(zip(lista1,lista2))

print('-----Zip lists-----')
print()
#usando list() temos ent uma lista de tuples
print(list(listas_juntas))
print(listas_juntas[0])
print()
# set
#Similar a listas
# Evita itens duplicados
# Não utiliza index
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]
num1 = set(list1)
num2 = set(list2)

print('----Funções de sets-----')
print()
#retorna novos sets
print(num1 | num2) #Union - junta dois sets deixando apenas um item de cada, itens não se repetem
print(num1 - num2) #difference - retorna somente os itens diferentes da primeira lista em relaçao a outra - retira da primeira oq é igual a segunda
print(num1 ^ num2) #Symetric diff - retorna somente os itens diferentes das duas listas, exclui oq é igual
print(num1 & num2) #and - retorna somente os itens iguais

print(num1.intersection(num2))
print(num1.union(num2))
print(num1.difference(num2))
print(num1.symmetric_difference(num2))
print()

print('-----Lambda, map e filter----')
print()

my_tuple = (1,1,2,3,4,5,6,7,8,9,10)
print(my_tuple.count(6))
print(tuple(map(lambda x: x+10, my_tuple)))
print(tuple(filter(lambda x: x%2 == 0, my_tuple)))
print()

print('----List comprehension-----')
print()

#isso
valores = [x * 2 for x in range(11)]
print(valores)
#em vez disso
# valores = []

# for x in range(11):
#     valores.append(x*2)

# print(valores)

print()

print('----Generators----')

numeros = [x*10 for x in range(10000)]
print(type(numeros))
print(getsizeof(numeros))

#parenteses é generator
numeros = (x*10 for x in range(10000))
print(type(numeros))
print(getsizeof(numeros))