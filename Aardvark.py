import language
import sys
Aardvark = language.Lang()
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
