#!/usr/bin/python
# -*- coding: utf-8 -*-

from carro import Carro  # importando a class
from veiculo import Veiculo

# instância do objeto carro
carro = Carro('cinza', 'ford', 'Marcus')

# print('O tipo de carro é: ', type(carro))
# print('Imprimindo um objeto carro...')
# print('Cor: '+carro.cor)
# print('Marca: '+carro.marca)
# print('Dono: '+carro.dono)

caminhao = Carro('branca', 'chevrolet', 'Antônio')

# print('\nImprimindo um objeto carro...')
# print('Cor: '+caminhao.cor)
# print('Marca: '+caminhao.marca)
# print('Dono: '+caminhao.dono)

carro.toString()
carro.abastecer(20)
print('tanque atual:', carro.tanque)
carro.abastecer(5)
print('tanque atual:', carro.tanque)

print('\n')
caminhao.toString()
caminhao.abastecer(40)
print('tanque atual:', caminhao.tanque)
caminhao.abastecer(10)
print('tanque atual:', caminhao.tanque)
