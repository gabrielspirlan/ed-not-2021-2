# ALGORITMO DE BUSCA BINARIA
# 
# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de
# busca, divide a lista em duas metades e procura pelo valor de busca
# apenas na metade onde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor de busca ou que reste apenas uma
# sublista vazia, quando se conclui que o valor de busca não existe na lista.

from time import time
from data.lista_nomes import nomes

def busca_binaria(lista, valor_busca):
     """
        Função que implementa o algoritmo de busca binária

        Retorna a posição onde valor_busca foi encontrado ou o valor convencional -1
        se valor_busca não existir na lista
    """
    ini = 0
    fim = len(lista) - 1 # Última posição

    while ini <= fim:
        # Dupla dupla barra faz uma divisão inteira, desconsiderando os decimais
        meio = (ini + fim) // 2
        
        # 1° caso: lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca:
            return meio # meio é a posição onde valor_busca está na lista
        # 2° caso: valor_busca é menor que lista [meio]
        elif valor_busca < lista[meio]:
            fim = meio - 1 # Descarta a 2° metade da lista
        
        # 3° caso: valor_busca é maior que lista[meio]
        else:
            ini = meio + 1 # Descarta a 1° metade da lista
        
    # 4° caso: valor_busca não encontrado na lista
    return -1

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'FAUSTO')}")
hora_fim = time()
print(f"Tempo gasto procurando FAUSTO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'ZULEICA')}")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'LUNISVALDO')}")
hora_fim = time()
print(f"Tempo gasto procurando LUNISVALDO: {(hora_fim - hora_ini) * 1000}ms")

