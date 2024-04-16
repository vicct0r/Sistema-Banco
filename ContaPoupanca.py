from Conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        if self._auth:
            valor_pos_saque = self.saldo - valor
            if valor_pos_saque >= 0:
                self.saldo -= valor
                self._extrato(f'SAQUE: {valor:.2f} R$')
            self._extrato(f'SAQUE RECUSADO: {valor:.2f} R$ ')
            return self.saldo
        print('PermissionError: Usuário não autênticado.')

