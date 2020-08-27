from Aardvark import *
@Aardvark.type("number")
def number(what, line_num):
    for i in str(what):
        if i not in "0123456789.+-*%^/":
            return False, what
    return True, eval(str(what))