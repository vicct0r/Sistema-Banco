from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, numero_da_conta: int, saldo=0, _auth: bool = False):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self._auth = False


    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass


    def depositar(self, valor: float) -> float:
        if self._auth:
            self.saldo += valor
            self._extrato(f'DEPOSITO EFETUADO: {valor:.2f}')
            return self.saldo
        print('PermissionError: Usuário não autênticado.')

    def _extrato(self, msg):
        print(f'{msg}')
        print(f'Saldo atual {self.saldo:.2f} R$')


    def __repr__(self):
        return f'{self.__class__.__name__!r}\nAgencia: {self.agencia!r}\nNúmero da Conta: {self.numero_da_conta!r}\nSaldo: {self.saldo!r}\nAuth: {self.autenticado}'