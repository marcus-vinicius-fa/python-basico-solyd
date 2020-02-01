#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

url = 'http://economia.awesomeapi.com.br/USD-BRL/'
querystring = {'format': 'json'}

response = requests.request('GET', url, params=querystring)

print('Moeda: ' + response.text['name'] + '\nMin: ' + response.text['low'] +
      ' / Máx: ' + response.text['high'])
