comps = 0
divisoes = 0
juncoes = 0

def merge_sort(lista):
    """
        Função que implementa o algoritmo merge sort usando o método recursivo
    """

    # Não podemos zerar as variáveis globais de estatística
    # dentro da função porque ela é recursiva e resetaria
    # a contagem a cada chamada
    global comps, divisoes, juncoes
    # Só continua se a lista tiver mais de um elemento
    if len(lista) > 1:
        meio = len(lista) // 2

        # Gera cópia da primeira metada da lista
        lista_esq = lista[:meio] # Do início ao meio - 1
        # Gera cópia da segunda metada da lista
        lista_dir = lista[meio:] # Do meio ao fim

        # Chamamos a recursividade a função para continuar
        # repartindo a lista em metade
        lista_esq = merge_sort(lista_esq)
        lista_dir = merge_sort(lista_dir)

        # Junta as duas metada em uma única lista, ordenada
        pos_esq = 0
        pos_dir = 0
        ordenada = [] # lista vazia

        # Compara os elementos de cada lista entre si e insere na
        # lista ordeanda a que for menor
        while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
            # O elemento que se encontra na lista da esquerda
            # é menor que o que se encontra na lista da direita
            if lista_esq[pos_esq] < lista_dir[pos_dir]:
                ordenada.append(lista_esq[pos_esq])
                pos_esq += 1
            # O contrário
            else:
                ordenada.append(lista_dir[pos_dir])
                pos_dir += 1
            comps += 1
        
        # No python não é possível declarar várias sem nada
        # Para isso cria-se uma variável igual a None
        sobra = None # A sobra da lista que ficou para trás

        if pos_esq < pos_dir: # Houve sobra à esquerda
            sobra = lista_esq[pos_esq:] # Sobra do pos_esq até o final
        
        else:
           sobra = lista_dir[pos_dir:] # Sobra do pos_dir até o final
        
        juncoes += 1
        return ordenada

######################################################
comps = 0
divisoes = 0
juncoes = 0
nums = [88, 44, 33, 0 , 99, 55, 77 , 22, 11, 66]


###############################################################
from data.nomes_desord import nomes
from time import time
import tracemalloc

comps = 0
divisoes = 0
juncoes = 0

ini = time()
tracemalloc.start() # Inicia a medição de consumo de memória

nomes_ord = merge_sort(nomes)

mem_atual, nem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes_ord)
print(f"Tempo: {fim - ini}")
print(f"Pico de memória: {nem_pico / 1024 / 1024}MB")
print(f"Comparações: {comps}, divisões: {divisoes}, junções: {juncoes}")

tracemalloc.stop() # Finaliza a medição do consumeo de memória

# Troca é uma das operações mais lentas por isso o Bublle sort e o selection sort tem
# eficiência menor que o merge sort

# Selection sort tenta otimizar a quantidade de trocas

# Merge Sort funciona a partir do dividir e conquistar, demonta tudo
# e muda tudo de novo. O problema é que ele ocupa muito espaço de memória 
# para realizar as trocas

