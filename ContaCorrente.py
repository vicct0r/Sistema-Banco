from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_da_conta: int, saldo: float=0, limite: float=0, _auth: bool = False):
        super().__init__(agencia, numero_da_conta, saldo, _auth)
        self.limite = limite


    def sacar(self, valor: float):
        if self._auth:
            valor_pos_saque = self.saldo - valor
            if valor_pos_saque < -self.limite:
                self._extrato(f'SAQUE RECUSADO: {valor:.2f} R$')
                return self.saldo
            else:
                self.saldo -= valor
                self._extrato(f'SAQUE EFETUADO: {valor:.2f} R$')
                return self.saldo
        print('PermissionError: Usuário não autênticado.')

    def __repr__(self):
        tipo_conta = self.__class__.__name__
        return f'{tipo_conta}\nNumero da Conta: {self.numero_da_conta!r}\nAgencia: {self.agencia!r}\nSaldo: {self.saldo!r}\nLimite: {self.limite!r}\nAuth: {self._auth}'