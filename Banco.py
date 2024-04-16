from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca


class Banco:
    def __init__(self, agencias: list | None = None, contas: list | None = None, clientes: list | None = None):
        self.agencias = []
        self.contas = []
        self.clientes = []


    def _checa_agencia(self, agencia_inserida):
        for agencia in self.agencias:
            if agencia_inserida == agencia:
                return True
        print(f'Agencia {agencia_inserida} não encontrada.')
        return False
    

    def _checa_conta(self, conta):
        for _conta in self.contas:
            if conta == _conta:
                return True
        print('Conta não encontrada.')
        return False


    def _checa_cliente(self, cliente):
        for _cliente in self.clientes:
            if cliente == _cliente:
                return True
        print('Cliente não registrado no sistema!')
        return False


    def autenticar(self, cliente: object):
        if self._checa_agencia(cliente.conta.agencia) and self._checa_cliente(cliente) and self._checa_conta(cliente.conta):
            print(f'Bem vindo {cliente.nome}!')
            cliente.conta._auth = True
            return True
        print(f'Cliente não cadastrado no sistema.')
        return False
