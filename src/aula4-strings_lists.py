frase = 'Aula 4 - Strings e Listas'

print(frase[0]) # -> 'A'

lista = [] # -> Array em outras linguagens

linguagens_de_programacao = ['Go', 'Python', 'JavaScript', 'Java', 'Ruby', 'PHP']

#                             0       1           2           3      4       5

# Array ou Lista possui índices para marcar a posição dos seus elementos.
# O primeiro índice é o 0 -> [0, 1, 2, 3, 4, 5]

print('\n')
print(linguagens_de_programacao)

print('\n')
print('Estou aprendendo ' + linguagens_de_programacao[1] + '!')

print('\n')
print(frase[0:6]) # Deve imprimir apenas -> Aula 4
# O espaço em branco conta como caracter!

print('\n')
print(frase[0:25])
print('\n')
print(frase[0:25:2]) # 'Steps' (o padrão é 1) -> Quantos pulos?

print('\n')
print('Estou estudando no momento:', linguagens_de_programacao[1:3])
# [1:3] -> Não imprime o 3, é até ele, mas ele mesmo não está incluso.

print('\n')
print('Esse é o último elemento ->', linguagens_de_programacao[-1])
# -1 -> conta os índices de trás pra frente. -2, -3 -4...

print('\n')
print('Frase ao contrário: ' + frase[::-1])
# '':'':-1 serve para imprimir tudo, mas ao contrário

### -> linguagens_de_programacao.'metodos de lista para utilizar' 

print('\n')
linguagens_de_programacao.append('C++') # O append adiciona no final da lista
print(linguagens_de_programacao)

print('\n')
linguagens_de_programacao.remove('Java') # Remove item desejado
print(linguagens_de_programacao)

print('\n')
linguagens_de_programacao.clear() # Remove todos os itens da lista
print(linguagens_de_programacao)

print('\n')
linguagens_de_programacao = ['Go', 'Python', 'JavaScript', 'Ruby', 'PHP', 'C++']
print('Antes do insert:', linguagens_de_programacao)

print('\n')
linguagens_de_programacao.insert(3, 'Java') # Diferente do append o insert me permite adicionar um item num local (posição) específica
print('Depois do insert:', linguagens_de_programacao)

print('\n')
linguagens_de_programacao[0] = 'Perl' # Modificar um dado na lista
print(linguagens_de_programacao)

print('\n')
print(linguagens_de_programacao.count('JavaScript')) # Quantas vezes aparece esse valor na lista?

print('\n')
print('Existêm', len(linguagens_de_programacao), 'dados na lista') # Quantos elementos têm na lista

print('\n')
print('Tirando o dado', linguagens_de_programacao.pop(), 'da pilha') # Funciona como pilha, tira o item do topo
print(linguagens_de_programacao)

### -> frase.'metodos para strings'

# len

print(frase.upper()) # TUDO MAIÚSCULO
print(frase.lower()) # tudo minúsculo
print(frase) # Os metodos acima não modificam, servem apenas para exibição

frase_lista = frase.split(' - ') # cria uma lista com o valor de frase separando com o '' + 'traço'+ '', poderia ser vírgula...
print(frase_lista)

frase_nova = '<' + frase + '>' # concatenação
print(frase_nova)