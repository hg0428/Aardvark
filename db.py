#Aardvark.library
from Aardvark import *
import json

@Aardvark.function('add')
def add(name, key, value, file='db.json'):
    data = {}
    data[f'{key}'] = f'{value}'
    json_data = json.dumps(data)
    with open(file, 'a') as database:
      database.write(json_data + ',')
    print(f'Data stored!\nData: {json_data}')

@Aardvark.function('get')
def get(name, key, data=json.loads('db.json')):
  for value in data.items():
    print(value)

'''
data['key'] = 'value'
json_data = json.dumps(data)
'''
