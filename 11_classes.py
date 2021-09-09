
# Este método é executado quando um objeto é criado a partir
# de uma classe (construtor)
def __init__ (self, base, altura, tipo = "R"):
    #recebe os valores passados ao construtor e os armazena
    # dentro dos atributos
    if base <= 0:
        raise Exception("A base deve ser maior que zero.")
    elif altura <= 0:
        raise Exception ("A altura deve ser maior que zero.")
    elif tipo not in ["R", "T", "E"]
        raise Exception("O tipo deve ser R, T ou E.")
    self.base = base
    self.altura = altura
    self.tipo = tipo
