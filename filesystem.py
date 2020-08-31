#Aardvark.library
from Aardvark import *

@Aardvark.function('newFile')
def newFile(name, filename, filevalue):
  with open(f'{filename}', 'w') as file:
    file.write(filevalue)
  print(f'{filename} succefully created!')

@Aardvark.function('openFileAndWrite')
def openFileAndWrite(name, filename, newvalue):
  with open(f'{filename}', 'r') as file:
    file.write(f'{newvalue}')