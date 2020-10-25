#Aardvark.library
from Aardvark import *
import random

@Aardvark.function("factorial")
def factorial(name, n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


@Aardvark.function("shuffle")
def shuffle(name, l):
    return sorted(l, key=lambda k: random.random())

@Aardvark.function("randomchoice")
def randomchoice(name, iterable):
  return random.choice(iterable)


@Aardvark.function("random")
def random_funct(name):
  return random.random()


@Aardvark.function("randint")
def randint(name, a, b):
  return random.randint(a, b)

@Aardvark.function("color_out")
def cp(text, color="white", style=0, back=0):
    print(gcolor(color, style, back) + text + "\x1b[0m", end="")