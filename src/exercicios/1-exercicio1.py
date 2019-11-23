'''
EXERCÍCIO 1: Faça um formulário que pergunte
o nome, cpf, endereço, idade, altura, e telefone
e imprima isso em um relatório organizado
'''

print('FORMULÁRIO\n')

nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
endereco = input('Digite seu endereço completo: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura [use o formato 1.70]: ')
telefone = input('Digite o seu telefone [Insira o DDD + 9 no início]: ')

print('\nDADOS CADASTRADOS CO SUCESSO!\nCONFIRA SEUS DADOS...')
print('\nSeu nome é', nome, ', com cpf de número:', cpf, '\nEndereço:', endereco,'\nIdade:', idade, 'anos\nAltura:', altura, '\nTelefone para contato:', telefone)