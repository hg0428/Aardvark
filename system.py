from Aardvark import *
#Aardvark.library
import sys, os

# Disable
@Aardvark.function("blockStdout")
def blockStdout(name):
    sys.stdout = open(os.devnull, 'w')

# Restore
@Aardvark.function("enableStdout")
def enableStdout(name):
    sys.stdout = sys.__stdout__