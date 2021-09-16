# Políndro: é um texto que, quando lido de trás para frente,
# mante´m o mesmo conteúdo (desprezando acentos e espaçamento)
# texto = "SOCORRAM-ME, SUBI NO ÔNIBUS EM MARROCOS"
texto = "BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHÃO"

pilha = []

# Percurso do palíndromo, colocando cada letra na lista
for letra in texto:
    pilha.append(letra)

print(pilha)

inverso = ""

# Retira cada letra da lista, de trás para frente, e coloca no inverso
while len(pilha) > 0:
    inverso += pilha.pop()   # pop() retira sempre o ÚLTIMO elemento

print(inverso)

# PILHA
# A pilha é um tipo abstrato de dados (TAD) que permite a entrada e a saída
# de dados apenas na sua extremidade final. Como consequência, ela segue a
# regra LIFO (last in, first out - último a entrar, primeiro a sair), e tem
# acesso limitado aos seus elementos.

# 2 + {3 - [5 * (2 + 7)]}

