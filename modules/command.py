from Aardvark import *
import subprocess
#Aardvark.library

@Aardvark.function("command")
def command_function(name, command):
    try:
        subprocess.run([command], check = True)
    except subprocess.CalledProcessError:
        error("Command Not Found", Aardvark.line_num, f'command({command})', f"Unknown command '{command}'")