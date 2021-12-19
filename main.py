import language
import os
import threading
import sys
import stringtype
import list
import boolean
import none
import number
import re
import memory_profiler
import File
import dictionaries
import functions
import urllib.request as urllib
"""
#ape Regex
#include Regex
funct a() {
  if 1==1 {
    output("yes")
  }
}
"""
end = ""
totry = ""


def fix(file='main.py'):
  f = open(file, "r").read().replace("\t", "  ")
  f = open(file, "w").write(f)
  print('Done!')


#fix("language/__init__.py")


def deleteKey(todelete, line_num):
  gt = Aardvark.gettype(todelete, line_num)
  del Aardvark.variables[todelete]
  for i in Aardvark.attributes[gt[0]]:
    del variables[todelete + "." + i[0]]


def returnKeyword(toreturn, line_num):
  toreturn = Aardvark.gettype(toreturn, line_num)[1]

  return toreturn


def continueKey(code, line_num):
  thread = threading.Thread(target=parse_line, args=(code, line_num))
  thread.daemon = True
  thread.start()


def maxmemory_statement(amount, line_num):
  global globalmaxmemory
  globalmaxmemory = amount


def ape_statement(file, line_num):
  try:

    url = f"https://aardvark-website.programit.repl.co/scripts/{file}"
    extensions = [".adk", ".py", "_adkmod.py"]
    for extension in extensions:
      try:
        req = urllib.urlopen(url + extension)
        ext = extension
        break
      except:
        pass
    f = str(req.read().decode('utf-8'))
    open(f"modules/{file}{ext}", "w+").write(f)
    cp(f"Sucessfully installed {file}", "green")
  except:
    error(
        "InstallationError", line_num, f"#ape {file}",
        f"{file} could not be installed, check the spelling and make sure its name has not changed in a recent update."
    )


def include_statement(inclusion, line_num):
  global end
  if inclusion == 'anr':
    functions.end = '\n'
    return None
  else:
    extensions = [".adk", ".py", "_adkmod.py"]
    for ext in extensions:
      try:
        if ext == ".adk":
          file = open(inclusion + ext).read().split("\n")
          for line in file:
            parse_line(line, line_num)
          return
        elif ext == ".py" or ext == "_adkmod.py":
          a = open("modules/" + inclusion + ext)
          sys.path.insert(1, f'modules')
          exec(a.read(), {}, {})
          return

      except FileNotFoundError:
        continue
    error("ImportError", line_num, f"#include {inclusion}",
          f"Module {inclusion} could not be found.")


def ifblock(code, line_num):
  code = code.split("\n")
  isif = regex["isif"].fullmatch(code[0]).groups()[0]
  #print(isif, Aardvark.gettype(isif, line_num))
  if Aardvark.gettype(isif, line_num)[1]:
    for i in code[1:]:
      returnvalue = parse_line(i, line_num)
      if returnvalue != None:
        return returnvalue


def whileblock(code, line_num):
  code = code.split("\n")[:-1]
  while Aardvark.gettype(iswhile, line_num)[1]:
    for i in code[1:]:
      returnvalue = parse_line(i, line_num)
      if returnvalue != None:
        return returnvalue


def newfunction(code, line_num):
  code = code.split("\n")
  isfunctiondefinition = regex["isfunctiondefinition"].fullmatch(
      code[0]).groups()
  argslist = Aardvark.gettokens(isfunctiondefinition[1], sep=",")
  Aardvark.adduserfunction(isfunctiondefinition[0], code[1:], argslist,
                           line_num)

  @Aardvark.function(isfunctiondefinition[0])
  def userfunction(name, *args):
    data = Aardvark.userfunctions[name]
    number = 0
    for i in args:
      if type(i) == str:
        i = i.replace("'", "\\'")
      makevar((data[1][number], i))
      #parse_line(f"{data[1][number]} = '{i}'", data[-1])
      number += 1
    keywords["isreturn"] = returnKeyword
    for i in data[0]:
      keywords["isreturn"] = returnKeyword
      returnvalue = parse_line(i, data[-1])
      if returnvalue != None:

        del keywords["isreturn"]
        return returnvalue


def forinblock(code, line_num):
  code = code.split("\n")[:-1]
  isforin = regex["isforin"].fullmatch(code[0]).groups()
  for i in Aardvark.gettype(isforin[1], line_num)[1]:
    parse_line(f"{isforin[0]} = {i}", line_num)
    for line in code[1:]:
      returnvalue = parse_line(line, line_num)
      if returnvalue != None:
        return returnvalue


def foreachblock(code, line_num):
  code = code.split("\n")[:-1]
  isforeach = regex["isforeach"].fullmatch(code[0]).groups()
  a = Aardvark.gettype(isforeach[1], line_num)[1].count(
      Aardvark.gettype(isforeach[0], line_num)[1])

  for i in range(a):
    for line in code[1:]:
      returnvalue = parse_line(line, line_num)
      if returnvalue != None:
        return returnvalue


def tryexceptblock(code, line_num):
  global totry
  code = code.split("\n")[:-1]
  blocks["iscatch"] = catchblock
  totry = code[1:]


def catchblock(code, line_num):
  global totry
  del blocks["iscatch"]
  code = code.split("\n")

  todo = regex["iscatch"].fullmatch(code[0]).groups()[0]
  try:

    for i in totry:

      parse_line(i, line_num)
  except AardvarkError as e:
    makevar([todo, f"'{e.error}'"])
    for i in code[1:-1]:
      parse_line(i, line_num)


from Aardvark import *
Aardvark.things = {
    "isif": ifblock,
    "iswhile": whileblock,
    "isforeach": foreachblock,
    "isforin": forinblock,
    "isfunctiondefinition": newfunction,
    "isinclude": include_statement,
    "isape": ape_statement,
    "ismaxmem": maxmemory_statement,
    "iscontinue": continueKey,
    "isdelete": deleteKey,
    "istryexcept": tryexceptblock
}
setupadk()
from Aardvark import *
instuff = []


def remove_comments(code):
  instring = ""
  comment = ""
  incomment = False
  newstring = ""
  for i in code:
    if i in "\"'" and not incomment:
      if i in instring:
        instring = instring[:-1]
      else:
        instring += i
    if i == "/" and not incomment and instring == "":
      incomment = True
      comment = ""
    if i == "\\" and incomment and instring == "":
      incomment = False
      i = ""
      comment = ""
    if not incomment:
      newstring += i
    if incomment:
      comment += i
  return newstring + comment


globalmaxmemory = 1000


def parse_line(line, line_num):
  done = False
  global instuff, globalmaxmemory
  if memory_profiler.memory_usage()[0] > globalmaxmemory:
    error("MemoryError", line_num, line,
          "The program went above its maximum memory.")
##################################################
  for block in blocks:
    regualrexp = regex[block].fullmatch(line)
    if regualrexp:
      instuff.append([blocks[block], ""])
  for i in Aardvark.gettokens(line, ["}"])[:-1]:
    what = instuff[-1]
    instuff = instuff[:-1]
    if len(instuff)==0:
      return what[0](what[1], line_num)
    for i in instuff:
      i[1] += line + "\n"
    return
  for i in instuff:
    i[1] += line + "\n"
  if len(instuff) > 0:
    return


##########################################################
  ismethod = Aardvark.gettokens(line, ["."])

  isfunction = regex["isfunction"].fullmatch(line)
  defvar = Aardvark.gettokens(line, ["="])
  if len(defvar)>1:
    return makevar(defvar)
  if isfunction:
    Aardvark.process_function(isfunction.groups()[0], line_num)
    return
  if len(ismethod)>1:

    return Aardvark.process_method(ismethod[0], ismethod[1], line_num)

  
  for i in statements:
    match = regex[i].fullmatch(line)
    if match:
      statements[i](match.groups()[0], line_num)
      return
  for key in keywords:
    match = regex[key].fullmatch(line)
    if match != None:

      done = True
      toreturnkey = keywords[key](match.groups()[0], line_num)
      return toreturnkey

  if re.fullmatch("[\t ]*", line):
    return
  else:
    if done == False:
      error("SyntaxError", line_num, line, "Invalid Syntax.")
global line_num
line_num = 0
print(
    "Aardvark Version 0.8.7 BETA\nUse the help function for help.\n© Copyright 2021 PlasDev, hg0428, ZDev1\n"
)
Aardvark.parse_line = parse_line
if len(sys.argv) == 1:
  while True:
    if memory_profiler.memory_usage()[0] > globalmaxmemory:
      error("MemoryError", line_num, a,
            "The program exceeded its maximum memory.")
    line_num += 1
    a = remove_comments(input(">>> "))
    try:
      parse_line(a, line_num)
    except Aardvark.AardvarkError as e:
      e.printtext()
      break
    except KeyboardInterrupt:
      error("KeyboardInterrupt", line_num, a, "")
    '''except Exception:
      try:
        error(
          "SyntaxError", line_num, a,
          "Unknown SyntaxError. This could be an error in your program or an error in the language."
          )
      except AardvarkError as a:
        a.printtext()'''

else:
  line_num = 0
  lines = open(sys.argv[-1]).read().split("\n")
  for line in lines:
    line_num += 1
    try:
      parse_line(line, line_num)
    except AardvarkError as e:
      e.printtext()
      break
    except Exception:
      try:
        error(
          "SyntaxError", line_num, a,
          "Unknown SyntaxError. This could be an error in your program or an error in the language."
        )
      except:
        break


#############################################
#############################################
#############################################
### © Copyright by hg0428, PlasDev, ZDev1 ###
#############################################
#############################################
#############################################
