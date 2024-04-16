from Cliente import Cliente
from Conta import Conta
from Pessoa import Pessoa
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Banco import Banco

#Criando objeto Conta
conta1 = ContaCorrente(201, 111)
conta1.sacar(200)# erro1

#Criando objeto Cliente
cliente1 = Cliente('Victor', 23)
cliente1.conta_usuario(conta1) 

#Criando objeto Banco
bancoBrasil = Banco()

#Testando
conta1.depositar(20) # erro2

#Adicionando usuário ao objeto Banco:
bancoBrasil.agencias.append(201)
bancoBrasil.clientes.append(cliente1)
bancoBrasil.contas.append(conta1)
conta1.depositar(10)# erro3

#Autenticando --Obs.:(Não deve ser possível fazer operações sem a conta estar autenticada):
bancoBrasil.autenticar(cliente1)

conta1.depositar(200.50)
conta1.sacar(20.10)
