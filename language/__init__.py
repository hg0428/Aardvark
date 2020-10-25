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
    re.compile("[\t ]*funct [\t ]*.+\(.*\)[\t ]*{[\t ]*"),
    "ismaxmem":
    re.compile("#max-memory[\t ]* (.+)"),
    "isreturn":
    re.compile("[\t ]*return[\t ]* (.+?)[\t ]*"),
    "isforeach":
    re.compile("[\t ]*for [\t ]*each [\t ]*(.+?) [\t ]*in [\t ]*(.+?)[\t ]*{")
}


class TYPE:
  def __init__(self, name, check):
    self.name = name
    self.attributes = {}
    self.methods = {}
    self.check = check

  def __repr__(self):
    return f"{self.name} data type"

  def AddAttr(self, name, calc):
    self.attributes[name] = calc

  def AddMethod(self, name, torun):
    self.methods[name] = torun


def hascommonelement(l1, l2):
  common = []
  for i in l1:
    if i in l2 and i not in common:
      common.append(i)
  return common


class AardvarkError(Exception):
  def __init__(self, error):
    self.error = error
    super().__init__(error)


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
  cp(f"Error on line {line}:\n{code}\n{etype}: {specific}", "red")
  raise AardvarkError(etype)
  sys.exit()


class Variable:
  def __init__(self, name, gt):
    self.name = name
    if gt == None:
      gt = ("none", "none")
    self.gt = gt
    self.type = gt[0]
    self.value = gt[1]
    self.attributes = {}

  def __repr__(self):
    return self.gt


class Lang:
  def __init__(self):
    self.line_num = 0
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
    self.types[fortype].AddAttr(name, calc)

  def function(self, name):
    def decorator_repeat(func):
      self.functions[name] = func

      self.variables[name] = Variable(name, ("function", func))

      def wrapper_repeat(*args, **kwargs):
        value = func(*args, *kwargs)
        return value

      return wrapper_repeat

    return decorator_repeat

  def type(self, name):
    def decorator_repeat(func):
      self.types[name] = TYPE(name, func)
      self.attributes[name] = []
      self.variables[name] = Variable(name, ("type", func))

      def wrapper_repeat(*args, **kwargs):
        value = func(*args, *kwargs)
        return value

      return wrapper_repeat

    return decorator_repeat

  def method(self, fortype, name):
    def decorator_repeat(func):
      self.methods[fortype, name] = [fortype, func]
      self.types[fortype].AddMethod(name, func)

      def wrapper_repeat(*args, **kwargs):
        value = func(*args, *kwargs)
        return value

      return wrapper_repeat

    return decorator_repeat

  def gettokens(self, text, sep=[","], returnremoved=False, ignore=[" ", "\t"], itemsdict={'"':'"', "'":"'", "(":")", "[":"]"}):
    removed = []
    t = ""
    wait = 0
    toreturn = []
    waitfori = 0

    for i in range(0, len(text)):
      if wait == 0:
        t += text[i]
      if text[i] not in list(itemsdict.keys()) and text[i] in ''.join(
          sep) and waitfori == 0:
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
      if text[i] in list(
          itemsdict.keys()) and wait == 0 and waitfori == 0:
        number = 0
        for item in text[i + 1:]:
          if item == itemsdict[text[i]]:
            waitfori = number + 2
            break
          number += 1
      if text[i] in ignore and waitfori == 0 and wait == 0:
        t = t[:-1]
      if wait != 0:
        wait -= 1
      if waitfori != 0:
        waitfori -= 1
    toreturn.append(t)
    if returnremoved == True:
      return toreturn, removed
    return toreturn

  def gettype(self, what, line_num, dontcheck=[]):
    self.line_num = line_num
    for t in self.types:
      if t not in dontcheck:
        try:
          check = self.types[t].check(what, line_num)
        except:
          check = (False, what)
        if check[0] == True:
          return t, check[1]
    what = str(what)
    ismethod = regex["ismethod"].fullmatch(what)
    isattribute = re.fullmatch(
        "[\t ]*(.+?)\.([A-Za-z\.][a-zA-Z0-9\.]*)[\t ]*", what)
    spilttered = self.gettokens(
        what, sep=["+", "-", "*", "/"], returnremoved=True)
    if isattribute:
      isattribute = isattribute.groups()
      calledon = self.gettype(isattribute[0], line_num)
      attributes = self.attributes[calledon[0]]
      for i in attributes:
        if i[0] == isattribute[1]:
          return self.gettype(i[1](calledon[1]), line_num)
    elif len(spilttered) > 0 and "added" not in dontcheck:
      try:
        final = self.gettype(
            spilttered[0][0], line_num, dontcheck=["added"])[1]
      except TypeError:
        return
      try:
        removed = spilttered[1]
        num = 0
        for i in spilttered[0][1:]:
          data = self.gettype(i, line_num, dontcheck=['added'])
          if data[0] == 'string':
            data = (data[0], f'"{data[1]}"')
          final = eval(f"{final} {removed[num]} {data[1]}")
          num += 1
      except TypeError:
        self.error("TypeError", line_num, what,
                   "Those items can not be added together.")
      if type(final) == str:
        final = f"'{final}'"
      return self.gettype(final, line_num, dontcheck=["added"])
    if re.fullmatch("[\t ]*([A-Za-z][a-zA-Z0-9]*[\t ]*\(.*?\)?)[\t ]*",
                    what):
      result = self.process_function(what, line_num)
      if type(result) == str:
        result = f'"{result}"'
      return self.gettype(result, line_num)
    elif ismethod:
      ismethod = ismethod.groups()
      result = self.process_method(ismethod[0], ismethod[1], line_num)
      if type(result) == str:
        result = f'{result}'
      return self.gettype(result, line_num)
    elif what in self.variables:
      return self.variables[what].gt
    self.error("TypeError", self.line_num, what,
               "That is not a valid datatype.")

  def process_function(self, function, line_num):
    self.line_num = line_num
    if not function.endswith(")"):
      self.error("SyntaxError", line_num, function,
                 "Function calls must start with '(' and end with ')'.")
    else:
      try:
        code = function[:-1].split("(", 1)
        function = self.functions[code[0].replace(" ", "").replace(
            "\t", "")]
      except KeyError:
        self.error("NameError", line_num, '('.join(code) + ")",
                   f"Function '{code[0]}' does not exist.")
      args = self.gettokens(code[1], [","])
      arguments = []
      for arg in args:
        if arg == '':
          continue
        arguments.append(self.gettype(arg, line_num)[1])
      try:
        returnvalue = function(code[0], *arguments)
        if returnvalue == None:
          returnvalue = "none"
        return returnvalue
      except TypeError:
        self.error("TypeError", line_num, '('.join(code) + ")",
                   "Incorrect number of arguments.")

  def process_method(self, calledon, method, line_num):
    calledon = self.gettype(calledon, line_num)
    if not method.endswith(")"):
      self.error("SyntaxError", line_num, method,
                 "Method calls must start with '(' and end with ')'.")
    else:
      try:
        code = method[:-1].split("(", 1)
        method = self.types[calledon[0]].methods[code[0].replace(" ", "").replace("\t", "")]
      except KeyError:
        self.error(
            "AttributeError", line_num, '('.join(code) + ")",
            f"'{calledon[0]}' object has no attribute '{code[0]}'.")
      args = self.gettokens(code[1], [","])
      arguments = []
      for arg in args:
        if arg == '':
          continue
        arguments.append(self.gettype(arg, line_num)[1])
      try:
        returnvalue = method(code[0], calledon[1], *arguments)
        if returnvalue == None:
          returnvalue = "none"
        return returnvalue
      except TypeError:
        self.error("TypeError", line_num, '('.join(code) + ")",
                   "Incorrect number of args.")
