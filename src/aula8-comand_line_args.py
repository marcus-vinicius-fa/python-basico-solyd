#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys  # Biblioteca que "conversa" com SO
from time import sleep

# Muito útil para criar scripts
argumentos = sys.argv

# arg1 = method // arg2 = num1 // arg3 = num2


def soma(num1, num2):
    return (num1) + (num2)


def sub(num1, num2):
    return (num1) - (num2)

# Criando command-lines...


if argumentos[1] == 'soma':  # argumentos é uma lista? O arg 0 é chamar o próprio programa
    resposta = soma(int(argumentos[2]), int(argumentos[3]))
    print('Somando...')
    sleep(1)
    print(str(resposta))

elif argumentos[1] == 'sub':
    resposta = sub(int(argumentos[2]), int(argumentos[3]))
    print('Subtraindo...')
    sleep(1)
    print(str(resposta))

# não precisa de um else, pois não tenho que usar argumentos obrigatoriamente ao rodar um arquivo.py
