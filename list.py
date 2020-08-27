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
            listtoreturn.append(Aardvark.gettype(i)[1])
        return True, listtoreturn
    else:
        return False, what