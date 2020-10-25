from Aardvark import *
import re


@Aardvark.type("dictionary")
def dictionary_type(what, line_num):
    if type(what)==dict:
      return True, what
    what=str(what)
    isdict = re.fullmatch("\{.*\}", what)
    if not isdict:
        return False, what
    what = Aardvark.gettokens(what[1:-1], [",", ":"])
    dicttoreturn = {}
    l1 = []
    number = 0
    for i in what:
        l1.append(Aardvark.gettype(i, line_num)[1])
    for i in range(len(l1)):
        if i % 2 == 0:
            dicttoreturn[l1[i]] = l1[i + 1]
    return dicttoreturn


@Aardvark.method("dictionary", "getitem")
def getdictitem(name, dictionary, item):
    try:
        return dictionary[item]
    except:
        error("ValueError", 0, f"{dictionary}.{name}({item})",
              f"{item} is not in {dictionary}")


@Aardvark.method("dictionary", "newitem")
def additem(name, dictionary, key, value):
    return dictionary.update({key: value})


def dict_length_attribute(thelist):
    return len(thelist)


Aardvark.addattribute("dictionary", "length", dict_length_attribute)

@Aardvark.function("makedict")
def makeDict(name):
  return {}