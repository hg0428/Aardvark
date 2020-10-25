#Aardvark.library
from Aardvark import *
import json


@Aardvark.function('addKey')
def add(name, key, value, file='db.json'):
    try:
        data = eval(open(file).read())
    except:
      error("JSONError", 0, f"addKey({key}, {value}, {file})", "The specified file is not in a valid format.")
    data[f'{key}'] = f'{value}'
    json_data = json.dumps(data)
    with open(file, 'w+') as database:
      database.write(json_data)
    print(f'Data stored!\nData: {json_data}')

@Aardvark.function('loadData')
def loadData(name, file="db.json"):
  data=open(file).read()
  print('Data:\n' + data)
  return data