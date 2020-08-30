import language
import os
import sys
from Aardvark import *
import stringtype
import list
import boolean
import none
import number
import re
from pathlib import Path
import memory_profiler
import File
import dictionaries
end = ""

'''
#include visual
visual("hello world", "700x700+10+20")
label('hello', 'black', 'white', 80, 150)
show()
'''


def inculde_statement(inclusion, line_num):
    global end
    if inclusion == 'anr':
        end = '\n'
        return None
    else:
        try:
            file = open(inclusion + ".adk").read().split("\n")

            for line in file:
                parse_line(line, line_num)
        except FileExistsError and FileNotFoundError:
            try:
                file = open(inclusion + ".py").read()
                if "from Aardvark import *" in file and "#Aardvark.library" in file:
                    exec(f"import {inclusion}")
            except FileExistsError and FileNotFoundError:
                error("ImportError", line_num, inclusion,
                      f"Module {inclusion} could not be found.")



@Aardvark.function(
    "dissable")  # Functions start with this, dissable is the functions name
def dissable_function(name,
                      inclusion):  #Argument is inclusion, name is always given
    global end
    if inclusion == 'anr':
        end = ""
        return None


@Aardvark.function('clear')
def clear(name):
    os.system('clear')
    print("Aardvark Version 0.2.5 BETA\nUse the help function for help.\nCopyright 2020 PlasDev, hg0428, ZDev1\n")


@Aardvark.function("open")
def open_function(name, file, mode="r"):
    return open(file, mode)


@Aardvark.function("mem")  #mem is this ones name
def memory(name, file):  #get the size of a file
    a = Path(file).stat().st_size
    print(f'{a} Bytes')
    return None


@Aardvark.function("output")  #
def output_function(name, toprint):  #Output function
    if end == "":
        print(toprint, end="")
    else:
        print(toprint)


@Aardvark.function("input")
def input_function(name, prompt):  #Input function
    return input(prompt)


@Aardvark.function("exit")
def exit_function(name):
    sys.exit()


@Aardvark.function("help")
def help_function(name):  #Help function
    print(
        "Go to: https://repl.it/@Programit/Aardvark-website#script.js we are still working on the site."
    )


@Aardvark.function("string")
def string_function(name, obj=""):
    return str(obj)


@Aardvark.function("number")
def number_function(name, obj=""):
    return float(obj)


@Aardvark.function("list")
def list_function(name, obj=""):
    return list(obj)


@Aardvark.function("boolean")
def boolean_function(name, obj=""):
    global line_num
    return boolean.Boolean(obj, line_num)[1]


@Aardvark.function("exec")
def exec_function(name, code, lang="Aardvark"):
    global line_num
    lang = lang.lower()
    if lang == "aardvark":
        for i in code.split("\n"):
            parse_line(i, line_num)
    elif lang == "python":
        exec(code)


def ifblock(code, line_num):
    code = code.split("\n")[:-1]
    isif = re.fullmatch("[\t ]*if [\t ]*(.+?)[\t ]*{[\t ]*",
                        code[0]).groups()[0]
    if Aardvark.gettype(isif, line_num)[1] == True:
        for i in code[1:]:
            parse_line(i, line_num)


def whileblock(code, line_num):
    code = code.split("\n")[:-1]
    iswhile = re.fullmatch("[\t ]*while [\t ]*(.+?)[\t ]*{[\t ]*",
                           code[0]).groups()[0]
    while Aardvark.gettype(iswhile, line_num)[1] == True:
        for i in code[1:]:
            #print(i)
            parse_line(i, line_num)


def newfunction(code, line_num):
    code = code.split("\n")[:-1]
    isfunctiondefinition = re.fullmatch(
        "[\t ]*funct [\t ]*(.+)\((.*)\)[\t ]*{[\t ]*", code[0]).groups()
    argslist = Aardvark.gettokens(isfunctiondefinition[1], sep=",")
    Aardvark.adduserfunction(isfunctiondefinition[0], code[1:], argslist,
                             line_num)
    @Aardvark.function(isfunctiondefinition[0])
    def userfunction(name, *args):
        data = Aardvark.userfunctions[name]
        number = 0
        for i in args:
          if type(i)==str:
            i = i.replace("'", "\\'")
          parse_line(f"{data[1][number]} = '{i}'", data[-1])
          number += 1
        for i in data[0]:
            a = parse_line(i, data[-1])
            if a != None:
                return a


def forinblock(code, line_num):
    code = code.split("\n")[:-1]
    isforin = re.fullmatch("[\t ]*for [\t ]*(.+) [\t ]*in [\t ]*(.+)[\t ]*{",
                           code[0]).groups()
    for i in Aardvark.gettype(isforin[1], line_num)[1]:
        parse_line(f"{isforin[0]} = {i}", line_num)
        for line in code[1:]:
            parse_line(line, line_num)


instuff = []


def remove_comments(code):
    instring = False
    incomment = False
    newstring = ""
    for i in code:
        if i in "\"'" and incomment == False:  #fixed
            if i == instring:
                instring = False
            else:
                instring = i
        if i == "/" and incomment == False and instring == False:
            incomment = True
        if i == "\\" and incomment == True and instring == False:
            incomment = False
            i = ""
        if not incomment:
            newstring += i
    return newstring





globalmaxmemory = 99999999999999999999999999999999999999999999999999999999999


def parse_line(line, line_num, enable_return=False):
    global instuff, globalmaxmemory
    if memory_profiler.memory_usage()[0] > globalmaxmemory:
        error("MemoryError", line_num, line,
                       "The program went above its maximum memory.")
    isfunction = re.fullmatch("[\t ]*([A-Za-z_][a-zA-Z0-9_]*[\t ]*\(.*?\)?)",
                              line)
    ismethod = re.fullmatch(
        "[\t ]*(.+)\.([A-Za-z_][a-zA-Z0-9_]*[\t ]*\(.*?\))", line)
    defvar = re.fullmatch(
        "[\t ]*([A-Za-z_][a-zA-Z0-9_]*)[\t ]*=[\t ]*(.+?)[\t ]*", line)
    isif = re.fullmatch("[\t ]*if [\t ]*(.+?)[\t ]*{[\t ]*", line)
    iswhile = re.fullmatch("[\t ]*while [\t ]*(.+?)[\t ]*{[\t ]*", line)
    isforin = re.fullmatch("[\t ]*for [\t ]*(.+) [\t ]*in [\t ]*(.+)[\t ]*{",
                           line)
    isinclude = re.fullmatch("[\t ]*#include [\t ]*(.+)", line)
    isfunctiondefinition = re.fullmatch(
        "[\t ]*funct [\t ]*.+\(.*\)[\t ]*{[\t ]*", line)
    ismaxmem = re.fullmatch("#max-memory[\t ]* (.+)", line)
    isreturn = re.fullmatch("[\t ]*return[\t ]* (.+?)[\t ]*", line)
    #print(instuff)
    if len(instuff) >= 1 and (isforin or isfunctiondefinition or iswhile or isif):
        instuff.append(["nothing", "nothing"])
    if re.fullmatch("[\t ]*}[\t ]*", line):
        what = instuff[-1]
        instuff = instuff[:-1]
        #print(instuff)
        if what[0]!="nothing":
          what[0](what[1], line_num)
    for i in instuff:
        i[1] += line + "\n"
    if len(instuff) > 0:
        return
    if isfunction:
        #print("PARSE FUNCTION")
        Aardvark.process_function(isfunction.groups()[0], line_num)
    elif defvar:

        defvar = defvar.groups()
        #print("Defvar is:", defvar)
        gt = Aardvark.gettype(defvar[1], line_num)
        Aardvark.variables[defvar[0]] = language.Variable(defvar[0], gt)
        for i in Aardvark.attributes[gt[0]]:
            Aardvark.variables[defvar[0] + "." + i[0]] = language.Variable(
                defvar[0] + "." + i[0], Aardvark.gettype(
                    i[1](gt[1]), line_num))
    elif ismethod:
        #print("method")
        ismethod = ismethod.groups()
        Aardvark.process_method(ismethod[0], ismethod[1], line_num)
    elif isif:
        instuff.append([ifblock, line + "\n"])
    elif iswhile:
        instuff.append([whileblock, line + "\n"])
    elif isforin:
        instuff.append([forinblock, line + "\n"])
    elif isinclude:
        #print("IT IS AN #include")
        inculde_statement(isinclude.groups()[0], line_num)
    elif isfunctiondefinition:
        #print("defining function")
        instuff.append([newfunction, line + "\n"])
    elif ismaxmem:
        globalmaxmemory = float(ismaxmem.groups()[0])
    elif isreturn and enable_return:
        return Aardvark.gettype(isreturn.groups()[0], line_num)


#output('hi'.replace('i', 'e'))
global line_num
line_num = 0
print("Aardvark Version 0.2.5 BETA\nUse the help function for help.\n© Copyright 2020 PlasDev, hg0428, ZDev1\n")
while True:
    #print(memory_profiler.memory_usage(), globalmaxmemory)
    if memory_profiler.memory_usage()[0] > globalmaxmemory:
        error("MemoryError", line_num, a,
                       "The program went above its maximum memory.")
    line_num += 1
    a = remove_comments(input(">>> "))
    parse_line(a, line_num)
    #This will do it after every line of code.
