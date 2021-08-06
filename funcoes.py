# Importar o valor da constante pi
# math é o nome da biblioteca onde pi se encontra
from math import pi

# Função é um trecho de código que tem um nome e pode receber informações externas para fazer seu trabalho. Opcionalmente, uma função pode também produzir um valor de resultado. Uma função é definida apenas uma vez e pode ser utilizada (chamada) várias vezes, evitando repetições de código.
# Existem funções já providas pela linguagem, como por exemplo, len(), range() e sort() e podemos definir também nossas próprias funções.

#Os termos que aparecem em parênteses são chamados parâmetros ou argumentos
# Quando uma função produz um valor de resultado usa return
def imc(peso, altura):  #Definição (ou declaração) da função
    """
        Função que calcula o Índice de Massa Corpórea(IMC)
    """
    # Trechos entre aspas triplas são um tipo especial de comentário chamado docstring, e servem para documentar o propósito de uma função ou classe.
    # peso / (altura)²
    return peso / altura ** 2


#float(): converte o valor informado em um número com casas decimais
#(flaoting point)
#p = float(input('Informe o peso da pessoa: '))
#a = float (input('Informe a altura da pessoa: '))

#Fazendo uma chamada à função imc()
#resultado = imc(p, a)
#print(resultado)

def area_forma(base, altura, forma = 'R'):
    '''
        Função que calcula a área de uma das seguintes
        formas geométricas: retângulo, triângulo ou elipse
        Parâmetro forma:
        "R" == retângulo (parâmetro opcional com valor padrão)
        "T" == triângulo
        "E" == elipse
    '''
    area = 0
    if forma == 'R': # Retângulo
        area = base * altura
    elif forma == 'T': # Triângulo
        area = base * altura / 2
    elif forma == 'E':
        area = (base / 2) * (altura / 2) * pi
    return area

print(f"Retângulo 7.5x11: {area_forma(7.5, 11, 'R')}")
print(f"Triângulo 8x12: {area_forma(8, 12, 'T')}")
print(f"Elipse 15x15: {area_forma(15, 15, 'E')}")
print(f"Quadrado 9.5x9.5: {area_forma(9.5, 9.5)}") # Seleciona o valor padrão na 3° parametro