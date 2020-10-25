import language
import sys
import re
global blocks, statements, keywords
Aardvark = language.Lang()
Aardvark.Aardvark=Aardvark
def makevar(defvar):
    gt = Aardvark.gettype(defvar[1], Aardvark.line_num)
    Aardvark.variables[defvar[0]] = language.Variable(defvar[0], gt)
    for i in Aardvark.attributes[gt[0]]:
        Aardvark.variables[defvar[0] + "." + i[0]] = language.Variable(
            defvar[0] + "." + i[0], Aardvark.gettype(i[1](gt[1]), Aardvark.line_num))
def setupadk():
    adk = Aardvark.things
    global blocks, statements, keywords
    blocks = {
        "isif": adk['isif'],
        "iswhile": adk['iswhile'],
        "isforeach": adk['isforeach'],
        "isforin": adk['isforin'],
        "isfunctiondefinition": adk['isfunctiondefinition'],
        "istryexcept":adk["istryexcept"]
    }

    statements = {
        "isinclude": adk['isinclude'],
        "isape": adk['isape'],
        "ismaxmem": adk['ismaxmem']
    }

    keywords = {
        "iscontinue": adk['iscontinue'],
        "isdelete": adk['isdelete'],
    }


colors = {
    "red": "31",
    "green": "32",
    "orange": "33",
    "blue": "34",
    "purple": "35",
    "lblue": "36",
    "white": "37",
    "black": "30"
}


class AardvarkError(Exception):
    def __init__(self, etype, code, line, specific):
      self.error=etype
      self.line=line
      self.code=code
      self.specific=specific
      super().__init__(error)
    def printtext(self):
      cp(f"Error on line {self.line}:\n{self.code}\n{self.error}: {self.specific}", "red")
      sys.exit()
      



def gcolor(color="white", style=0, back=0):
    a = colors[color]
    style = str(style) + ";"
    back = ";" + str(back)
    if back == ";0":
        back = ""
    return "\x1b[" + style + a + back + "m"


def cp(text, color="white", style=0, back=0):
    print(gcolor(color, style, back) + text + "\x1b[0m")


def error(etype, line, code, specific):

    raise Aardvark.AardvarkError(etype, code, line, specific)
    return Aardvark.AardvarkError(etype, code, line, specific)

Aardvark.error = error
Aardvark.AardvarkError=AardvarkError
regex = {
    "ismethod":
    re.compile("[\t ]*(.+)\.([A-Za-z_][a-zA-Z0-9_]*[\t ]*\(.*?\))"),
    "isfunction":
    re.compile("[\t ]*([A-Za-z_][a-zA-Z0-9_]*[\t ]*\(.*?\)?)"),
    "defvar":
    re.compile("[\t ]*([A-Za-z_][a-zA-Z0-9_]*)[\t ]*=[\t ]*(.+?)[\t ]*"),
    "isif":
    re.compile("[\t ]*if [\t ]*(.+?)[\t ]*{[\t ]*"),
    "iswhile":
    re.compile("[\t ]*while [\t ]*(.+?)[\t ]*{[\t ]*"),
    "isforin":
    re.compile("[\t ]*for [\t ]*(.+) [\t ]*in [\t ]*(.+)[\t ]*{"),
    "isinclude":
    re.compile("[\t ]*#include [\t ]*(.+)"),
    "isape":
    re.compile("[\t ]*#ape [\t ]*(.+)"),
    "isfunctiondefinition":
    re.compile("[\t ]*funct [\t ]*(.+)\((.*)\)[\t ]*{[\t ]*"),
    "ismaxmem":
    re.compile("#max-memory[\t ]* (.+)"),
    "isforeach":
    re.compile("[\t ]*for [\t ]*each [\t ]*(.+?) [\t ]*in [\t ]*(.+?)[\t ]*{"),
    "isreturn":
    re.compile("[\t ]*return [\t ]*(.+?)[\t ]*"),
    "iscontinue":
    re.compile("[\t ]*continue [\t ]*(.+?)[\t ]*"),
    "isdelete":
    re.compile("[\t ]*delete [\t ]*(.+?)[\t ]*"),
    "istryexcept":re.compile("[\t ]*try {"),
    "iscatch":re.compile("[\t ]*catch[\t ]* [\t ]*(.+?)[\t ]*{[\t ]*")
}
