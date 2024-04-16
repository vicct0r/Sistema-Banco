class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


    @property
    def _nome(self):
        return self.nome
    

    @_nome.setter
    def _nome(self, novo_nome: str):
        self.nome = novo_nome


    @property
    def _idade(self):
        return self.idade


    @_idade.setter
    def _idade(self, nova_idade: int):
        self.idade = nova_idade

