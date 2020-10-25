from Aardvark import *
#Aardvark.library
import sys, os
defvar("ARGV", sys.argv)

# Disable
@Aardvark.function("blockStdout")
def blockStdout(name):
    sys.stdout = open(os.devnull, 'w')


# Restore
@Aardvark.function("enableStdout")
def enableStdout(name):
    sys.stdout = sys.__stdout__


@Aardvark.function('newFile')
def newFile(name, filename, filevalue):
    with open(f'{filename}', 'w+') as file:
        file.write(filevalue)
    print(f'{filename} succefully created!')


@Aardvark.function("bash")
def bashcommand(name, command):
  os.system(command)