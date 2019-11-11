'''
EXERCÍCIO 2:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
e decide se ela está apta a ser do Exército. Para entrar no Exército é
preciso ter 18 anos ou mais de idade pesar mais ou igual a 60 kilos e medir 
mais ou igual a 1.70 metros.
'''

print('Esse programa avalia se você você está apto para servir seu País no Exército!\n')
input('Faremos algumas perguntas, você está preparado? [Press ENTER]')

idade = input('Digite sua idade: ')
peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

# Lógica do programa
if idade >= '18' and peso >= '60' and altura >= '1.70':
  print('\nParabéns você está apto!')
else:
  print('\nInfelizmente você não está apto.')

# A comparação >=, <=.. Funciona com strings (TESTAR) é por conta do python3?

## Ou converter os inputs para int e float e 
# comparar no if com 'tipos numéricos' (int ou float)