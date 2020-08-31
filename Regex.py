#Aardvark.library
from Aardvark import *
import re


@Aardvark.function("regex_match")
def regex_match(name, expr, item):
    return bool(re.fullmatch(expr, item))
