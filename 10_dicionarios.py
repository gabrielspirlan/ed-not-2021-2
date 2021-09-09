# Dicionário é uma estrutura de linguagem Python
# capaz de armazenar múltiplos valores

pessoa = {
    # "nome" é a chave
    # "Fulano de Tal" é o valor
    "nome": "Fulano de Tal",
    "sexo": "M",
    "idade": 39,
    "peso": 76,
    "altura": 1.82
}



# Calculando o IMC (Índice de Massa Corporal)
imc = pessoa["peso"] / (pessoa["altura"] ** 2)
print(f"O IMC de {pessoa['nome']} é {imc}.")


forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" 
}

forma2 = {
    "base": 6,
    "altura": 2.5
    "tipo": "T"
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"
}

def calcular_area(forma):
    if forma["tipo"] == "R":
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E"
        return forma["base"] / 2 * forma["altura"] / 2 * pi
    else: 
        #GERA UM ERRO
        raise Exception("Tipo de forma não reconhecido.")