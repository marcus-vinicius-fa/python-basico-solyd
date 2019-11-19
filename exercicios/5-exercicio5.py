'''
EXERCÍCIO 5: Crie um programa de gerenciamento bancário.
Ele deve ser capaz de criar clientes e contas. Cada cliente 
possui nome, cpf, idade. Cada conta possui um cliente, 
um saldo, um limite, sacar e depositar e consultar saldo
'''

# criando as classes num mesmo arquivo por somente para fins de exercício, e para variar

class Cliente:

  def __init__(self, nome, cpf, idade):
    self.nome = nome
    self.cpf = cpf
    self.idade = idade

#=========================================================

class Conta:

  def __init__(self, cliente, saldo, limite):
    self.cliente = cliente
    self.saldo = saldo
    self.limite = limite

  # TODO: Ajustar este método?
  def sacar(self, valor): 
    if valor <= self.saldo:
      if valor > self.limite:
        print('Operação não permitida!\nSeu limite é de R$' +str(self.limite) + ' e você tentou sacar R$' +str(valor))
      else:
        self.saldo -= valor
        print('Saque no valor de R$' + str(valor) + ' efetuado com sucesso!')
    else:
      print('Operação não permitida!\nVocê tentou sacar R$' +str(valor) + ' porém o seu saldo é de R$' +str(self.saldo))

  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor

  def consultar(self):
    return 'Saldo: R$'+str(self.saldo)

#=========================================================

cliente = Cliente('Marcus', '123.456.789-12', 25)
conta = Conta(cliente, 10, 100)

print('nome do cliente: '+conta.cliente.nome)
print('cpf do cliente: '+conta.cliente.cpf)
print('idade do cliente: '+str(conta.cliente.idade))

print('\n')

print(conta.consultar())

conta.depositar(490)
print(conta.consultar())

# conta.sacar(200)

conta.sacar(100)
print(conta.consultar())
conta.sacar(101)
print(conta.consultar())
conta.sacar(500)
print(conta.consultar())

conta.sacar(100)
print(conta.consultar())
conta.sacar(100)
print(conta.consultar())
conta.sacar(100)
print(conta.consultar())
conta.sacar(100)
print(conta.consultar())
conta.sacar(100)
print(conta.consultar())