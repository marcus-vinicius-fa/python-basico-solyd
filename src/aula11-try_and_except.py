#!/usr/bin/python
# -*- coding: utf-8 -*-

# bloco de tratamento de possíveis erros.

import time
# ou from time import sleep (ou ainda -> import*)

try:  # try = tentar
    a = 'abc' + 1
    print(a)

except Exception as erro:  # Exceções no geral. Classe pai das exceptions
    print('Erro:', erro)

# ===================================================================

try:
    b = 10 / 0
    print(b)

# except:
#   print('Erro: Divisão por zero!')
    # se eu errar a digitação aqui haverá uma exceção,
    # porque tratando uma except apareceu uma except

    # funcao() -> o erro não será tratado porque esse bloco espera uma except do tipo divisão por zero.
except ZeroDivisionError as erro:  # nomeando uma exception
    print('Erro:', erro)

print('>>> Aqui continua funcionando!')

# ===================================================================

# Exemplo de uma aplicação


def abrir_arquivo():
    try:
        arquivo = open('arquivo-aula11.txt', 'r')
        print('Arquivo existe, imprimindo seu conteudo:\n', arquivo.read())
        arquivo.close()
        return True  # só chega aqui se a instrução anterior não der uma exception

    except Exception as erro:
        print('Erro:', erro)
        return False

# ===================================================================


# while not abrir_arquivo(): # not False = True
continuar = True
while continuar:
    if abrir_arquivo():
        continuar = False
    else:
        time.sleep(5)
    # a função sleep() pausa as instruções do programa por 'x' segundos

# Após iniciar a execução do programa aguarde 10 segundos
# e crie um arquivo chamado 'arquivo-aula11.txt' e verifique
# as saídas no terminal.

# Se preferir abra outro terminal e execute em paralelo o arquivo 'aula11-exec' para
# criar automaticamente o arquivo 'arquivo-aula11.txt' com um delay de 20 segundos
