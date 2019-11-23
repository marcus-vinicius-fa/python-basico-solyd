# Bibliotecas internas do Python
# import sys
# import time

# Importação de bibliotecas externas
# pip - Gerenciador de pacotes Python

# pip install requests
# pip3 install requests

# python -m pip install requests
# python3 -m pip install requests

# url lib - biblioteca padrão do Python para trabalhar com web
import requests

# requisicao = requests.get('https://solyd.com.br/')

# requisicao = requests.post('https://solyd.com.br/')

# requisicao = requests.delete('https://solyd.com.br/')

# requisicao = requests.put('https://solyd.com.br/')

# requisicao = requests.get('https://solyd.com.br/testando-requisicoes')

# try:
#   print(requisicao,'\n')

#   print(requisicao.status_code,'\n')

#   print(requisicao.text,'\n')

#   print(requisicao.headers,'\n')

#   print(type(requisicao),'\n')
# except Exception as erro:
#   if erro: print(erro)

# Beautiful Soap 4 - bs4: Biblioteca para trabalhar com páginas html
# PutsReq

header = {'User-agent': 'Linux Mint 20'} # Dicionário # Mesma estrutura de um JSON
cookies = {'Ultima-visita': '23-11-2019'}
data = {'username': 'Marcus Vinicius',
        'password': '12345678'}


text = None # Nenhum (vazio)
try:
  request = requests.post('https://putsreq.com/DAbKjyyoQRRUZW0Ccpm8',
  headers=header,
  cookies=cookies,
  data=data) # headers é um parametro de requests
  

  text = request.text
except Exception as error:
  print('Erro: ',error)

print(text)