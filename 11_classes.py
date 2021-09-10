
# Este método é executado quando um objeto é criado a partir
# de uma classe (construtor)
def __init__ (self, base, altura, tipo = "R"):
    #recebe os valores passados ao construtor e os armazena
    # dentro dos atributos
    if type(base) not in [int, float] or base <= 0:
        raise Exception("A base deve ser númerica e maior que zero.")
    elif type(altura) not in [int, float] or altura <= 0:
        raise Exception ("A altura deve ser númerica e maior que zero.")
    elif tipo not in ["R", "T", "E"]
        raise Exception("O tipo deve ser R, T ou E.")
    self.base = base
    self.altura = altura
    self.tipo = tipo

    # Getter um método que possibilita saber o valor de um atributo
    # privado do lado de fora da classe
    def __get_base(self):
        return self.__base

    # Setter é um método que possibilita alterar o valor de um atributo
    # privando inclusive do lado de fora da classe
    def __set_base(self, valor):
        if type(valor) not in[int, float] or valor <= 0:
            raise Exception(' * A base deve ser númerica e maior que zero')
        self.__base = valor
    
    # property "esconde" as funções getter e setter dentro do nome de
    # um atributo, tornando mais simples a manipulação do objeto
    base = property(__get_base, __set_base)

    # Essas linhas começadas com @ são chamadas "decorators"
    # Os decarators instruem o Python a criar uma property com
    # um getter e um setter na hora da execução
    @property
    def altura(self):       # Getter para a propriedade chamada "altura"
        return self.__altura
    
    @altura.setter
    def altura(self, valor):    # Setter para a propriedade chamda "altura"
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception("* A altura deve ser númerica e maior que zero")
        self.__altura = valor
    


retangulo1.base = 9.6 # vai executar set_base da classe
