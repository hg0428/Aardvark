import language
from Aardvark import *
import string
import number
import list
import boolean
import none
import re


@Aardvark.function("output")
def output_function(name, toprint):  #Output function
    print(toprint, end="")
    return None


@Aardvark.function("input")
def input_function(name, prompt):  #Input function
    return input(prompt)


@Aardvark.function("exit")
def exit_function(name):
    sys.exit()


@Aardvark.function("help")
def help_function(name):  #Help function
    print(
        "Go to: https://github.com/hg0428/Aardvark and read README.md.\nLater on you will be able to use https://aardvark.readthedocs.io but we are still working on that site."
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
    return bool(obj)


@Aardvark.function("exec")
def exec_function(name, code, lang="Aardvark"):
    lang = lang.lower()
    if lang == "aardvark":
        for i in code.split("\n"):
            parse_line(i)
    elif lang == "python":
        exec(code)


def parse_line(line, line_num):
    isfunction = re.fullmatch("[\t ]*([A-Za-z][a-zA-Z0-9]*[\t ]*\(.*?\)?)",
                              line)
    ismethod = re.fullmatch("[\t ]*(.+)\.([\w][\w0-9]*[\t ]*\(.*?\))", line)
    if isfunction:
        #print("PARSE FUNCTION")
        Aardvark.process_function(isfunction.groups()[0], line_num)
    elif ismethod:
        ismethod = ismethod.groups()
        Aardvark.process_method(ismethod[0], ismethod[1], line_num)


#output('hi'.replace('i', 'e'))
line_num = 0
print("Aardvark 2 Version 0.0.1 BETA\nUse the help function for help.\n")
while True:
    line_num += 1
    parse_line(input(">>> "), line_num)
