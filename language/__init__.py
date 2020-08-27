import re
import sys
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


def hascommonelement(l1, l2):
    common = []
    for i in l1:
        if i in l2 and i not in common:
            common.append(i)
    return common


def gcolor(color="white", style=0, back=0):
    a = colors[color]
    style = str(style) + ";"
    back = ";" + str(back)
    if back == ";0":
        back = ""
    return "\x1b[" + style + a + back + "m"


def cp(text, color="white", style=0, back=0, end="\n"):
    print(gcolor(color, style, back) + text + "\x1b[0m", end=end)


def error(etype, line, code, specific):
    cp(f"Error on line {line}:\n{code}\n{etype}: {specific}", "red")
    sys.exit()


class Variable:
    def __init__(self, name, gt):
        self.name = name
        self.gt = gt
        self.type = gt[0]
        self.value = gt[1]

    def __repr__(self):
        return self.gt


class Lang:
    def __init__(self):
        self.functions = {}
        self.types = {}
        self.variables = {}
        self.classes = {}
        self.methods = {}

    def function(self, name):  #Lang.function() wrapper
        def decorator_repeat(func):
            self.functions[name] = func

            #self.variables[name] = Variable(name, ("function", func))

            def wrapper_repeat(*args, **kwargs):
                value = func(*args, *kwargs)
                return value

            return wrapper_repeat

        return decorator_repeat

    def type(self, name):  #Lang.type() wrapper
        def decorator_repeat(func):
            self.types[name] = func

            def wrapper_repeat(*args, **kwargs):
                value = func(*args, *kwargs)
                return value

            return wrapper_repeat

        return decorator_repeat

    def method(self, fortype, name):  #Lang.method() wrapper
        def decorator_repeat(func):
            self.methods[fortype, name] = [fortype, func]

            def wrapper_repeat(*args, **kwargs):
                value = func(*args, *kwargs)
                return value

            return wrapper_repeat

        return decorator_repeat

    def gettokens(self, text, sep=[""],
                  returnremoved=False):  #separates tokens
        if text == '':
            return text
        if sep == "":
            sep = [self.token_seperator]
        instring = False
        inpar = False
        num = 0
        t = ""
        s = ""
        tokens = []
        removed = []
        for i in str(text):
            s += i
            t += i
            common = hascommonelement(s, sep)
            if i in "\"'":
                s = ""
                if instring == False:
                    instring = i
                else:
                    instring = False
            if i in "()":
                s = ""
                if instring == False:
                    inpar = i
                else:
                    inpar = False
            elif len(common) > 0 and instring == False and inpar == False:
                tokens.append(t[:-len(common[0])])
                removed.append(common[0])
                s = ""
                t = ""
            elif i == " " and instring == False and inpar == False:
                i = ""
                t = t[:-1]
            elif len(s) == len(max(sep, key=len)):
                s = ""
            num += 1
        if instring == False:
            tokens.append(t)
        if returnremoved == True:
            return tokens, removed
        return tokens

    def gettype(self, what, line_num, dontcheck=[]):
        what = str(what)
        for t in self.types:  #Checks data types
            if t not in dontcheck:
                check = self.types[t](what, line_num)
                if check[0] == True:
                    return t, check[1]
        isfunction = re.fullmatch("[\t ]*([A-Za-z][a-zA-Z0-9]*[\t ]*\(.*?\)?)",
                                  what)
        ismethod = re.fullmatch("[\t ]*(.+)\.([\w][\w0-9]*[\t ]*\(.*?\)?)",
                                what)
        if isfunction:
            result = self.process_function(isfunction.groups()[0], line_num)
            if type(result) == str:
                result = f'"{result}"'
            return self.gettype(result, line_num)
        if ismethod:
            ismethod = ismethod.groups()
            result = self.process_method(ismethod[0], ismethod[1], line_num)
            if type(result) == str:
                result = f'"{result}"'
            return self.gettype(result, line_num)

    def process_function(self, function, line_num):
        if not function.endswith(")"):
            error("SyntaxError", line_num, function,
                  "Function calls must start with '(' and end with ')'.")
        else:
            try:
                code = function[:-1].split("(", 1)
                function = self.functions[code[0].replace(" ", "").replace(
                    "\t", "")]
            except:
                error("NameError", line_num, '('.join(code) + ")",
                      f"Function '{code[0]}' does not exist.")
            args = self.gettokens(code[1], [","])
            arguments = []
            for arg in args:
                arguments.append(self.gettype(arg, line_num)[1])
            return function(code[0], *arguments), "BYE"

    def process_method(self, calledon, method, line_num):
        calledon = self.gettype(calledon, line_num)
        if not method.endswith(")"):
            error("SyntaxError", line_num, method,
                  "Method calls must start with '(' and end with ')'.")
        else:
            try:
                code = method[:-1].split("(", 1)
                method = self.methods[(calledon[0],
                                       code[0].replace(" ", "").replace(
                                           "\t", ""))][1]
            except:
                error("NameError", line_num, '('.join(code) + ")",
                      f"'{calledon[0]}' object has no attribute '{code[0]}'.")
            args = self.gettokens(code[1], [","])
            arguments = []
            for arg in args:
                arguments.append(self.gettype(arg, line_num)[1])
            return method(code[0], calledon[1], *arguments)
