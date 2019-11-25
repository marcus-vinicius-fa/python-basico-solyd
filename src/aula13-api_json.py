# API: Interface para que a aplicação possa alcançar um serviço
# JSON - JavaScript Object Notation: Formatação de apresentação de dados

# Payload: Carga útil 

import requests
import json # serve para transformar objetos em dicionários python
from time import sleep

'''
Coódigo gerado por -> httpsnippet (Encontrei no Insomnia)

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
  title_movie = input('Qual filme vocễ gostaria de buscar? (informe o nome em inglês)\n->')

  response = None
  try:
    response = requests.get('http://www.omdbapi.com/?t='+title_movie+'&apikey=2398b6d5')
    dic = json.loads(response.text) # convertendo de json para dicionário
    return dic
  except Exception as error:
    print('Erro:',error)

filme = search_movie()
# TODO: print(filme)

print('\nFilme:',filme['Title'], 
      '\nAtores:',filme['Actors'],
      '\nAno:',filme['Year'], 
      '\nDiretor:',filme['Director'],
      '\nNota:',filme['imdbRating'])