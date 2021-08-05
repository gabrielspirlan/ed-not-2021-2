#range(): gera uma faixa de números

for i in range(10):
    print(i)

print('------------------------------------------------')

# range() com 2 argumentos: gera uma lista de números
# começando pelo primeiro argumento(inclusive) até o segundo argumento(exclusive)
for j in range(5,15):
    print(j)

print('------------------------------------------------')

# range() com três argumentos:
# 1°: limite infeior (inclusive)
# 2°: limite superior (exclusive)
# 3°: incremento ou passo (de quanto em quanto a lista irá andar)
for k in range(1,20,3):
    print(k)

print('------------------------------------------------')

for n in range(10, 0, -1):
    print(n)

