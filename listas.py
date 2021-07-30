#Criando uma lista
primos =[2, 3, 5, 7, 11, 13, 17, 19, 23,29]

#percurso
for num in primos:
    print(num)

#Acrescentar um novo elemento no FIM da lista: append()
primos.append(31)
print(primos)

#Inseridno um elemento em uma posição específica: insert()
#1° -> informa a posição de inserção
#2° -> elemento a ser inserido
primos.insert(0,1)
print(primos)

#Insere o valor 37 na posição 5
primos.insert(5, 37)
print(primos)

#retirnado o último elemento da lista: pop()
ultimo = primos.pop()
print(f'ultimo: {ultimo}')
print(primos

#removendo por valor: remove()
primos.remove(37)
print(primos)

#removendo por posição: del
#removendo o elemento da posição 4
primos.del(4)
print(primos)

#Fatiando uma lista
#Exibindo apenas do elemento da posição 0 (inclusive) à posição (exclusive)
print(primos[0:7])

#da Posição 2 à posição 8
print(primos[2:8])

#fatiando e criando uma sublista
sub_primos = primos[1:5]
print(sub_primos)