#!/usr/bin/python
# -*- coding: utf-8 -*-

# Coleções:

nomes_list = ['Marcus', 'Sâmela']  # lista
# melhor usada para listar itens

nomes_tuple = ('Marcus', 'Sâmela')  # tupla // não é mutável!
# Na tupla dá pra pegar o valor dos objetos ou edita-los, mas não adicionar
# e remover, ela não muda de tamanho.
# Quando utilizar? Quando o numero de objetos na lista não form mutável

# dicionário // key-value (chave-valor)
pessoa_dict = {'nome': 'Marcus', 'idade': 25}
# outra forma de declarar um dicionário
ling_end_framework_dict = dict(java='spring', javascript='node')
# // semelhante ao JSON no JavaScript
# // semelhante ao Hash-map (tabela hash) no Java

nomes_set = {'Marcus', 'Sâmela'}  # conjunto
# É uma lista misturada com dicionário
# Qual a diferença para lista?
# Não têm chave e valor, somente valores!
# Não pode haver itens repetidos!
# Não têm indice!

# Apenas a tupla não é dinámica.

print(type(nomes_list), '\n', type(nomes_tuple),
      '\n', type(pessoa_dict), '\n', type(nomes_set))

print(nomes_tuple[1])

# podem ser usados com for, para iterar

print(nomes_tuple)
nomes_tuple = ('Sâmela', 'Marcus')  # têm que substituir a tupla toda!
print(nomes_tuple)

if 'Marcus' in nomes_tuple:
    print('Marcus está na tupla!')
    # serve para todos menos dicionario...

if 'Marcus' in pessoa_dict.values():
    print('Marcus está na tupla!')

print(pessoa_dict)
# uso da chave para buscar o valor // a chave é única
print(pessoa_dict['nome'])
# muito eficiente para busca!

print(len(pessoa_dict))
print(len(nomes_set))

for values in pessoa_dict.values():  # .keys para ver as chaves
    print(values)  # não necesáriamente imprime na ordem

pessoa_dict['nome'] = 'Vinicius'
print(pessoa_dict)

pessoa_dict['altura'] = 1.85
print(pessoa_dict)

linguagens_set = {'Java', 'JavaScript'}
linguagens_set.add('Java')
# Não vai funcionar porque conjuntos não possuem itens iguais!
print(linguagens_set)

# caso ouvessem muitos itens uma busca na lista seria custosa enquanto no conjunto não!
# o conjunto é uma tabela hash, a lista é encadeada.
# nomes_list
# nomes_set
# if nome in nomes_list: buscar olhando todas as listas
# if nome in nomes_set: busca quase que instantânea

# Como inicializar essas coleções vazias?

lista = []
tupla = ()
dicionario = {}  # ou dicionario = dict()
conjunto = set()
