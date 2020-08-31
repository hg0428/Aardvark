#Aardvark.library
from Aardvark import *
import json

data = open('db.json').read()

@Aardvark.function('addKey')
def add(name, key, value, file='db.json'):
    data = {}
    data[f'{key}'] = f'{value}'
    json_data = json.dumps(data)
    with open(file, 'a') as database:
      database.write(json_data)
    print(f'Data stored!\nData: {json_data}')

@Aardvark.function('loadData')
def loadData(name):
  print('Data:\n' + data)
  return data
'''
data['key'] = 'value'
json_data = json.dumps(data)
'''
