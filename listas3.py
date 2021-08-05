# Lista de Strings
frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# imprimendo apenas a fruta "uva"
print(frutas[2])

# Substituindo "pera" por "melão"
frutas[3] = "melão"
print(frutas[3])

print('------------------------------------------------------')

# descobrindo elementos da lista
print(len(frutas))

print('------------------------------------------------------')

# Percorrendo e imprimindo cada uim dos elementos da lista
for fruta in frutas:
    print(fruta)


print('------------------------------------------------------')

# Percorrendo e imprimindo cada elemento e sua posição
for i in range(len(frutas)):
    print(f"{frutas[i]} está na posição {i}")

print('------------------------------------------------------')

# Percurso em orrdem invertida
# 1° argumento: len(frutas) - 1: a lista precisa começar no último elemento, que é determinado por len() - 1
# 2° argumento: -1, porque o limite final não entra e precisamos terminar em 0
# 3° argumento: para a lista percorrer de forma contrária, decaindo os números a cada passagem
for j in range(len(frutas) -1, -1, -1):
    print(frutas[j])

print('------------------------------------------------------')

# Ordenando o vetor em ordem alfabética
frutas.sort()
print(frutas)