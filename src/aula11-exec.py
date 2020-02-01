#!/usr/bin/python
# -*- coding: utf-8 -*-

# esse programa foi criado para criar um arquivo automaticamente
# e assim testar e verificar o funcionamento do try e except da aula 11

import time


def criar_arquivo():
    time.sleep(20)
    arquivo = open('arquivo-aula11.txt', 'w')
    arquivo.write('arquivo-aula11.txt')
    arquivo.close()
    print('verifique se o arquivo foi criado no diretório')


criar_arquivo()
