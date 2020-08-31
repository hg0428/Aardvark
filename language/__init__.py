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
    #print(l1, l2, common)
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
        self.attributes = {}

    def __repr__(self):
        return self.gt


class Lang:
    def __init__(self):
        self.functions = {}
        self.types = {}
        self.variables = {}
        self.methods = {}
        self.attributes = {}
        self.userfunctions = {}

    def adduserfunction(self, name, code, args, line_num):
        self.userfunctions[name] = [code, args, line_num]

    def addattribute(self, fortype, name, calc):
        self.attributes[fortype].append([name, calc])

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
            self.attributes[name] = []

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

    def gettokens(self,text, sep=[","], returnremoved=False):
        removed = []
        t = ""
        wait = 0
        toreturn = []
        waitfori=0
        itemsdict = {"'": "'", '"': '"', "(": ")"}
        for i in range(0, len(text)):
            if wait == 0:
                t += text[i]
            if text[i] not in list(itemsdict.keys()) and text[i] in ''.join(sep) and waitfori==0:
                new = ""
                number = 0
                for item in text[i:]:
                    new += item
                    if new in sep:
                        removed.append(new)
                        t = t[:-1]
                        toreturn.append(t)
                        t = ""
                        wait = number + 1
                        break
                    number += 1
            if text[i] in list(itemsdict.keys()) and waitfori==0 and wait==0:
                number = 0
                for item in text[i+1:]:
                    if item==itemsdict[text[i]]:
                        waitfori=number
                        break
                    number += 1
            if wait != 0:
                wait -= 1
            if waitfori!=0:
              waitfori-=1
        toreturn.append(t)
        if returnremoved:
            return toreturn, removed
        return toreturn

    def gettype(self, what, line_num, dontcheck=[]):
        #print(f"Getting the type of: {what}")
        for t in self.types:  #Checks data types
            if t not in dontcheck:
                try:
                    check = self.types[t](what, line_num)
                except:
                    check = (False, what)
                #print("Check:", t, check)
                if check[0] == True:
                    return t, check[1]
        what = str(what)
        ismethod = re.fullmatch("[\t ]*(.+)\.([\w][\w0-9]*[\t ]*\(.*?\)?)",
                                what)
        isattribute = re.fullmatch(
            "[\t ]*(.+?)\.([A-Za-z\.][a-zA-Z0-9\.]*)[\t ]*", what)
        spilttered = self.gettokens(
            what, sep=["+", "-", "*", "/"], returnremoved=True)
        #print("CHECKING")
        if isattribute:
            #print("ATTRIBUTE")
            isattribute = isattribute.groups()
            calledon = self.gettype(isattribute[0], line_num)
            attributes = self.attributes[calledon[0]]
            for i in attributes:
                if i[0] == isattribute[1]:
                    return self.gettype(i[1](calledon[1]), line_num)
        #print("WHAT:",what)
        elif len(spilttered) > 0 and "added" not in dontcheck:
            #print("MULTIPLE ADDED TOGETHER")
            try:
                final = self.gettype(
                    spilttered[0][0], line_num, dontcheck=["added"])[1] #calles gettype which calls gettokens
            except: #it will break if it does
                return None #
            try:
                removed = spilttered[1]
                num = 0
                for i in spilttered[0][1:]:
                    exec(
                        f"final {removed[num]}= self.gettype(i, line_num, dontcheck=[\"added\"])[1]"
                    )
                    num += 1
            except:
                error("TypeError", line_num, what,
                      "Those items can not be added together.")
            if type(final) == str:
                final = f"'{final}'"
            return self.gettype(final, line_num, dontcheck=["added"])
        if re.fullmatch("[\t ]*([A-Za-z][a-zA-Z0-9]*[\t ]*\(.*?\))[\t ]*",
                        what):
            #print(f"GETTYPE is sending {what} to process_function")
            result = self.process_function(what, line_num)
            if type(result) == str:
                result = f'"{result}"'
            return self.gettype(result, line_num)
        elif ismethod:
            #print("METHOD")
            ismethod = ismethod.groups()
            result = self.process_method(ismethod[0], ismethod[1], line_num)
            if type(result) == str:
                result = f'"{result}"'
            return self.gettype(result, line_num)
        elif what in self.variables:
            #print("VARIABLE")
            return self.variables[what].gt

    def process_function(self, function, line_num):
        #print("Function is:", function)
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
            print(code)
            args = self.gettokens(code[1], [","])
            print(args)
            arguments = []
            for arg in args:
                arguments.append(self.gettype(arg, line_num)[1])
            return function(code[0], *arguments)

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