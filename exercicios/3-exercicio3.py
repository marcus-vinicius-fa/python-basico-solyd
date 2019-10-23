'''
EXERCICIO: Faça um programa que leia a quantidade de 
pessoas que serão convidadas para uma festa. 

Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados.

Após isso irá imprimir todos os nomes da lista
'''

quant_pessoas = int(input('Quantas pessoas viram para a festa?\n -> '))

lista_convidados = []

print('\nDigite o nome de cada convidado\n')
for i in range(quant_pessoas):
  lista_convidados.append('- ' + input('Nome do convidado: '))

print('Todos os convidados estão na lista agora!')

input('press ENTER para ver a lista...')

print('\n')
i = 0

while i < len(lista_convidados):
  print(lista_convidados[i])
  i += 1