from Aardvark import *
@Aardvark.type("bool")
def Boolean(what, line_num):
    #print("Boolean",what)
    separated = Aardvark.gettokens(
        what,
        sep=["==", ">", "<", "!=", "<=", ">=", " and ", " or ", " not "],
        returnremoved=True)
    isboolean = False
    for i in [
            "==", ">", "<", "!=", "<=", ">=", " and ", " or ", "true", "false",
            " not "
    ]:
        if i in separated[0] or i in separated[1]:
            isboolean = True
    if isboolean == False:
        #print('FALSE', end="")
        return False, what
    newtext = ""
    number = 0
    for i in separated[0]:
        if i in ["true", "false", "none"]:
            newtext += i.capitalize()
        else:
            #print("else")
            a = Aardvark.gettype(i)
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
    #print(eval(newtext))
    return True, eval(newtext)


@Aardvark.function("output")
def output_function(name, toprint):  #Output function
    print(toprint, end="")
    return None