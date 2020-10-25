from Aardvark import *


@Aardvark.type("string")  #This is how you make a type
def string_type(what, line_num):
    what = str(what)
    instring = False
    instringcount = 0
    count = 0
    for i in str(what):
        if instring != False:
            instringcount += 1
        if i in "\"'" and i == instring:
            if count != len(str(what)) - 1:
                instringcount = 0
            instring = False
        if i in "\"'" and instring == False:
            instring = i
        count += 1
    if instringcount == len(
            str(what)) - 1 and instringcount > 0 and what[0] == what[-1]:
        if what[0] != what[-1]:
            language.error("TypeError", line_num, what,
                           "Strings must start and end with the same ' or \"")
        return True, eval(what.replace("\n", "\\n"))

    else:
        return False, what


@Aardvark.method("string", "replace")
def string_replace(name, string, old, new):
    return string.replace(old, new)


@Aardvark.method("string", "character")  #Here is a method for string types
def string_atindex(name, string, index):
    return string[index]


@Aardvark.method("string", "lower")
def string_lowercase(name, string):
  return string.lowe()


@Aardvark.method("string", "upper")
def string_uppercase(name, string):
  return string.upper()



def string_length_attribue(string):
    return len(string)


Aardvark.addattribute("string", "length", string_length_attribue)
