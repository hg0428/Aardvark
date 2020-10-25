

from Aardvark import *

import re


#Aardvark.library

@Aardvark.function("basicColor")
def basicColor_function(name, text, color):
    basicColors = {
        "black" : "\u001b[30m",
        "red" : "\u001b[31m",
        "green" : "\u001b[32m",
        "yellow" : "\u001b[33m",
        "blue" : "\u001b[34m",
        "magenta" : "\u001b[35m",
        "cyan" : "\u001b[36m",
        "white" : "\u001b[37m",
        "reset" : "\u001b[0m"
    }



    try:
        return f"{basicColors.get(color)}" + text + "\u001b[38;5;$0m"
    except:
        print("[!] WARNING! COLOR NOT FOUND")
        return f"{basicColors.get('reset')}{text}\u001b[38;5;$0m"

@Aardvark.function("customColor")
def customColor_function(name, text, id):
    id = int(id)
    if id > 256:
        print("[!] WARNING! THIS MODULE ONLY SUPPORTS 256 colors! You are exceeding the color limit D:")
        return "\u001b[38;5;$0m" + text + "\u001b[38;5;$0m"
    return f"\u001b[38;5;${id}m{text}\u001b[38;5;$0m"

@Aardvark.function("resetColor")
def resetColor_function(name, text):
    return f"\u001b[38;5;$0m{text}"




@Aardvark.type("Bold")
def bold(what, line_num):
    what = str(what)
    ismynewtype = re.fullmatch("Bold\((.*?)\)", what)
    if ismynewtype:
        return True, f"\u001b[1m{ismynewtype.groups()[0]}"

    else:
        return False, what

@Aardvark.type("Reverse")
def reverse(what, line_num):
    what = str(what)
    ismynewtype = re.fullmatch("Reverse\((.*?)\)", what)
    if ismynewtype:
        return True, f"\u001b[7m{ismynewtype.groups()[0]}"

    else:
        return False, what

@Aardvark.type("Underline")
def underline(what, line_num):
    what = str(what)
    ismynewtype = re.fullmatch("Underline\((.*?)\)", what)
    if ismynewtype:
        return True, f"\u001b[7m{ismynewtype.groups()[0]}"

    else:
        return False, what