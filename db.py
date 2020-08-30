#Aardvark.library
from Aardvark import *
import json

@Aardvark.function('addKey')
def add(name, key, value, file='db.json'):
    data = {}
    data[f'{key}'] = f'{value}'
    json_data = json.dumps(data)
    with open(file, 'a') as database:
      database.write(json_data + ',')
    print(f'Data stored!\nData: {json_data}')

@Aardvark.function('loadData')
def loadData(name, file="db.json"):
  print(open(file).read())

#@Aardvark.function('getKey')
#def get(name, key, data=open('db.json').read()):
#  for key, value in data.items():
#    print(value)

'''
data['key'] = 'value'
json_data = json.dumps(data)
'''
