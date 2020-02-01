#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Fazer um programa que consuma a API AMDBAPI para buscar livros usando os parametros 's' e 
'page'
'''

import requests
import json
from time import sleep

url = 'http://www.omdbapi.com/?apikey=2398b6d5'

querystring = {
    'type': 'movie',
    's': '',
    'page': '1-100',
}

payload = ''
# data=payload

# response = requests.request('GET', url, params=querystring)


def search_titles():
    titles = []
    title = input('Digite o nome do título\n>>>')
    querystring['s'] = str(title)

    print('Carregando resultados...')
    for i in range(1, 101):
        querystring['page'] = i
        response = requests.request('GET', url, params=querystring)
        response_dic = json.loads(response.text)
        if response_dic['Response'] == 'True':
            for movie in response_dic['Search']:
                titles.append(movie['Title'] + ' (' + movie['Year'] + ')')
        else:
            i = 101  # (ou break)

    print('\n', len(titles), 'resultados encontrados')
    print('\nResultados para título buscado:\n')
    sleep(1)
    return titles


response = search_titles()
for i in response:
    print(i)
