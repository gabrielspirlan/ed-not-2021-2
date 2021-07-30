
#print(): exibe informações
print("Olá, mundo!'")

#input(): permite a entrada de informações
nome = input('Qual é o seu nome? ')

print(f'olá, {nome}')

#int() converte o que foi informado no input() de texto para número inteiro
idade = int(input('informe a sua idade: '))

if idade >= 18:
    print('Você já pode beber.')
    print('Você já pode tirar habilitação')
else:
    print('Você não pode beber.')
    print('Você não pode tirar habilitação')