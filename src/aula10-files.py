#!/usr/bin/python
# -*- coding: utf-8 -*-

# open('C:\\Users\\marvi\\Desktop\\arquivo.txt') # \\ porque \ é palavra reservada no python

# open('arquivo.txt', 'w') # w -> write -> escrita
# o default é 'r' -> read -> leitura

# open('arquivo.txt', 'w') fazendo de novo eu sobrescrevo o arquivo

# Arquivos de texto (.txt)
# 'r', 'w', 'r+'(lê e escreve), 'a'(modo append, não sobrescreve)

# Outros arquivos (.'imagem', .exe)
# open(arquivo.ext, 'b')

# PARA ESCREVER:

arquivo = open('arquivo-aula10.txt', 'w')  # abrir no modo 'a'
print(type(arquivo))

arquivo.write('Escrevendo no arquivo\n')

for i in range(1, 11):
    arquivo.write(str(i)+'\n')

arquivo.write('\n')

for i in range(-10, 0):
    arquivo.write(str(-1*i)+'\n')

# FECHAR ARQUIVO

arquivo.close()

# PARA LER:

arquivo = open('arquivo-aula10.txt', 'r')

print(arquivo.read())

for linha in arquivo:
    print(linha)
