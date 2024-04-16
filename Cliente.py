from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta = None


    def conta_usuario(self, conta: object):
        self.conta = conta


    def __repr__(self):
        return f'Titular: {self.nome} \nIdade: {self.idade} \nConta: {self.conta.__class__.__name__}'

