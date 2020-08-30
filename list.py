from Aardvark import *
import re
@Aardvark.type("list")
def list_type(what, line_num):
    what = str(what)
    islist = re.fullmatch("\[.*?\]", what)
    if islist:
        separate = Aardvark.gettokens(what[1:-1], [","])
        listtoreturn = []
        for i in separate:
            listtoreturn.append(Aardvark.gettype(i, line_num)[1])
        return True, listtoreturn
    else:
        return False, what
@Aardvark.method("list", "push")
def list_push(name, thelist,toadd):
  return thelist.append(toadd)

@Aardvark.method("list", "pull")
def list_pull(name, thelist, topull):
  return thelist.remove(topull)
def list_length_attribute(thelist):
  return len(thelist)
Aardvark.addattribute("list", "length", list_length_attribute)