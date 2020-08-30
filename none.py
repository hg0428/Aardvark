from Aardvark import *
@Aardvark.type("none")
def none(what, line_num):
    what=str(what)
    if what == "none":
        return True, "none"
    else:
        return False, what
