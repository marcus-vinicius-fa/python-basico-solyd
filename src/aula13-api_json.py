#!/usr/bin/python
# -*- coding: utf-8 -*-

# API: Interface para que a aplicação possa alcançar um serviço
# JSON - JavaScript Object Notation: Formatação de apresentação de dados

# Payload: Carga útil

import requests
import json  # serve para transformar objetos em dicionários python
from time import sleep

'''
Código gerado por -> httpsnippet (Encontrei no Insomnia)

url = 'http://www.omdbapi.com/?'

querystring = {'t': 'avengers'}

payload = ''

response = requests.request('GET', url, data=payload, params=querystring)

print(response.text)
'''

'''
Aqui está sua chave: 2398b6d5

Anexe-a a todas as suas solicitações de API,

API OMDb: http://www.omdbapi.com/?i=tt3896198&apikey=2398b6d5

Usa-se o & ('I comercial') para adicionar novos parametros a url
'''
# exit() # Serve para parar a aplicação


def search_movie():
    title_movie = input(
        'Qual filme vocễ gostaria de buscar? (informe o nome em inglês)\n>>>')

    response = None
    try:
        response = requests.get(
            'http://www.omdbapi.com/?apikey=2398b6d5&type=movie&t='+title_movie)
        return response
    except Exception as error:
        print('Erro:', error)


def data_movie():
    try:
        # convertendo de json para dicionário
        movie_dic = json.loads(search_movie().text)
    except Exception as error:
        print('Erro:', error)

    # if movie_dic['Response'] == False:
    #   print('Filme não existe...')

    try:
        print('\nFilme:', movie_dic['Title'],
              '\nAtores:', movie_dic['Actors'],
              '\nAno:', movie_dic['Year'],
              '\nDiretor:', movie_dic['Director'],
              '\nNota:', movie_dic['imdbRating'],
              '\nCapa:', movie_dic['Poster'])

    except KeyError:
        print('Título não existe!')
    except Exception as error:
        print('Erro:', error)

# MAIN


data_movie()

continuar = True
while continuar:
    resp = input(
        '\nDeseja fazer mais uma busca? (s) para "SIM" e (n) para "NÃO"\n>>>')
    if resp.lower() == 's':
        data_movie()
    elif resp.lower() == 'n':
        continuar = False
        print('Saindo...')
        sleep(1)
    else:
        print('\nNão entendi sua escolha...')
