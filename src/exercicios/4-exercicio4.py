#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
EXERCÍCIO 4: 

Escreva uma função que recebe um objeto de coleção(um colecao)
de numeros e retorna o valor de maior número dentro dessa coleção.

Escreve uma função que retorna o menor valor.
'''


def maior_numero(colecao):
    maior = colecao[0]
    for i in colecao:
        if i > maior:
            maior = i
    return maior


def menor_numero(colecao):
    menor = colecao[0]
    for i in colecao:
        if i < menor:
            menor = i
    return menor


numeros = [10, 30, 25, 35, 70, 5, 3, 5, 20, 4, 2, 7, 9, 100]

print(numeros)
print('maior: ' + str(maior_numero(numeros)) +
      '\nmenor: ' + str(menor_numero(numeros)))
