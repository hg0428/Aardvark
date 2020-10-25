from Aardvark import *
import re


@Aardvark.type("list")
def list_type(what, line_num):
  if type(what)==tuple or type(what)==list:
    return True, list(what)
  what = str(what)
  islist = re.fullmatch("\[.*?\]", what)
  if islist:
    separate = Aardvark.gettokens(what[1:-1], [","])
    listtoreturn = []
    if len(separate)==1:
      return True, []
    for i in separate:
      if i!="":
        listtoreturn.append(Aardvark.gettype(i, line_num)[1])
    return True, listtoreturn
  else:
    return False, what


@Aardvark.method("list", "push")
def list_push(name, thelist, toadd):
  thelist.append(toadd)
  return thelist


@Aardvark.method("list", "pull")
def list_pull(name, thelist, topull):
  return thelist.remove(topull)


def list_length_attribute(thelist):
  return len(thelist)


Aardvark.addattribute("list", "length", list_length_attribute)

@Aardvark.method("list", "indexes")
def indexlist(name, thelist, start, end=-1):
  return thelist[start:end]

@Aardvark.method("list", "atindex")
def listatindex(name, thelist, index):
  return thelist[index]