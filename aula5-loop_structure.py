linguagens = ['Go', 'Python', 'JavaScript', 'Java', 'Ruby', 'PHP']

print(linguagens)

print(linguagens[2])
print('\n')

# For -> PARA cada..

for linguagem in linguagens: # diferente de outras linguagens!
  print(linguagem) # linguagem é o 'i'(índice da lista a cada iteração do for)

# Range

print('\n')
numeros = range(5, 10) # range(5, 10, 1) step default # range(5) = 0...5
for i in numeros:
  print(i)

print('\n')
for i in range(0, 101):
  print(i)

print('\nNumeros pares')
for i in range(2, 101, 2):
  print(i)

print('\n')
for i in range(len(linguagens)): # Quando não se sabe o tamanho da lista!
  print(linguagens[i])

print('\n')
numeros = []

for i in range(10): # Populando uma lista com for!
  numeros.append(i)

print(numeros)

print('\n')
frase = 'Aula 5 - Estrutura de laço'

for letra in frase: # iterando um string que também é uma coleção # 'letra' é um item
  print(letra)
print('\n')

# While -> ENQUANTO
# quando não sei até quando vai iterar

i = 0
while i < 10: # semelhante ao if
  print('i ainda é', i, 'potanto é menor que 10!')
  i += 1 # mesmo que i = i + 1
print('Acabou o while, pois, i agora é', i)

# Loop infinito

# i = 0
# while True:
#   print('Loop infinito: ', i)
#   i += 1

print('\n')
linguagens = ['Go', 'Python', 'JavaScript', 'Java', 'Ruby', 'PHP']

# se não existisse o 'len' -> print(len(linguagens))
count = 0 # contador

for i in linguagens:
  count += 1
print('A lista possui', count, 'linguagens')

# BREAK
print('\n')

i = 0
while True:
  print(i)
  if i == 20:
    break
  i += 1
print('Saiu do while true')