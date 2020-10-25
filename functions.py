from Aardvark import *
global end
end=""



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
    print(
        "Aardvark Version 0.7.4\nUse the help function for help.\n© Copyright 2020 PlasDev, hg0428, ZDev1\n"
    )


@Aardvark.function("open")
def open_function(name, file, mode="r"):
    return open(file, mode)


@Aardvark.function("currentMemUsage")
def currentMemUsage(name):
    return memory_profiler.memory_usage()[0]


@Aardvark.function("file_size")  #mem is this ones name
def file_size(name, file):  #get the size of a file
    a = Path(file).stat().st_size
    print(f'{a} Bytes')
    return a


@Aardvark.function("output")  #
def output_function(name, toprint):  #Output function
    global end
    print(toprint, end=end)


@Aardvark.function("input")
def input_function(name, prompt):  #Input function
    return input(prompt)


@Aardvark.function("exit")
def exit_function(name):
    sys.exit()


@Aardvark.function("help")
def help_function(name):  #Help function
    print("Goto: https://aardvark-website.programit.repl.co")


@Aardvark.function("string")
def string_function(name, obj=""):
    return str(obj)


@Aardvark.function("number")
def number_function(name, obj=""):
    return float(obj)


@Aardvark.function("list")
def list_function(name, obj=""):
    return list(obj)


@Aardvark.function("type")
def type_function(name, obj):
    gt=Aardvark.gettype(obj, Aardvark.line_num)
    return f'{gt[0]}'


@Aardvark.function("boolean")
def boolean_function(name, obj=""):
    global line_num
    return boolean.Boolean(obj, line_num)[1]


@Aardvark.function("exec")
def exec_function(name, code, lang="Aardvark"):
    global line_num
    lang = lang.lower()
    if lang in ["aardvark", 'adk']:
        for i in code.split("\n"):
            parse_line(i, line_num)
    elif lang in ["python", 'py']:
        exec(code, {}, {})

    else:
        error(
            "CodeExecutionError", Aardvark.line_num, f"{code}",
            f"Could not execute the given code in the specified language because the language: {lang} is not currently supported"
        )
