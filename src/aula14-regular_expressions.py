#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Padrões

# email -> email @ dominio.com.br

# Tel -> 99 99999-9999

# CPF -> 111.222.333-44

# regex
import re
import requests

# string_teste = 'O gato é bonito'

# # r -> raw String # string 'crua'
# print(r'Primeira linha\nSegunda linha')

# # 2 parâmetros ('expressão regular(padrão)', 'string')
# padrao = re.search(r'gat.', string_teste)

# if padrao:
#     print(padrao.group())  # para imprimir para .search
# else:
#     print('Padrão não encontrado')

# r'gat.' -> qualquer caracter (Inclusive '')
# r'gat\w' -> qualquer letra (Não encontra '')
# r'\w\w\w\w' -> qualquer palavra que tem 4 letras (acha a primeira palavra com esse padrão)...

# re.findall(r'gat\w') # print(padrao) // sem .group
# re.findall(r'gat\w+') # print(padrao) // + -> repete 1 ou mais vezes
# re.findall(r'gat\w*') # print(padrao) // * -> repete 0 ou mais vezes
# re.findall(r'gat\w+\.') # print(padrao) // \ -> para escapar caracters especiais
# re.findall(r'[gat]') # print(padrao) // [] -> quero uma letra desde que esteja dentro dos colchetes
# re.findall(r'[gat]+') # print(padrao) // []+ -> quero 1 ou mais letras das que estão
# re.findall(r'\w{4,6}') # print(padrao) // \w{4,6} -> palavras com 4 a 6 letras
# re.findall(r'a{3}') # print(padrao) // a{3} -> só se tiver 3 'a's

string = requests.get('http://lacoxinha.com.br/')

padrao = re.findall(r'[\w\.\_\-]+@[\w\-]+[\w\.\-]+', string.text)

if padrao:
    print('Email: ' + padrao + '\nÉ válido!!!')
else:
    print('Este não é um email válido!')
