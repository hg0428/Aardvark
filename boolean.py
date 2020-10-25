from Aardvark import *

@Aardvark.type("bool")
def Boolean(what, line_num):
    what=str(what)
    #print("Boolean",what)
    separated = Aardvark.gettokens(
        what,
        sep=["==", ">", "<", "!=", "<=", ">=", " and ", " or ", " not "],
        returnremoved=True)
    #print(separated)
    isboolean = False
    for i in [
            "==", ">", "<", "!=", "<=", ">=", " and ", " or ", "True", "False",
            " not "
    ]:
        if i in separated[0] or i in separated[1]:
            isboolean = True
    if isboolean == False:
        return False, what
    newtext = ""
    number = 0
    #print("starting loop")
    for i in separated[0]:
        #print("NEW",newtext)
        if i in ["True", "False", "none", " in "]:
            newtext += i
        else:
            a = Aardvark.gettype(i, line_num, dontcheck=["bool", "none", ])
            if a[0] == "string":
                toadd = f"'{a[1]}'"
            else:
                toadd = str(a[1])
            newtext += toadd
        try:
            newtext += separated[1][number]
        except:
            pass
        number += 1
    #print(newtext,eval(newtext))
    return True, eval(newtext)


@Aardvark.method("bool", "not")
def notmethod(name, boolean):
  return not boolean