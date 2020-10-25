from Aardvark import *
import _io
import re


@Aardvark.type("file")
def File(what, line_num):
    isfile=re.fullmatch("<?_io.TextIOWrapper ?name='(.*?)' ?mode='(.*?)'.+?", str(what))
    if type(what) == _io.TextIOWrapper:
        return True, what
    if isfile:
        isfile=isfile.groups()
        return True, open(isfile[0], isfile[1])
    else:
        return False, what


@Aardvark.method("file", "write")
def write_to_file(name, file, towrite):
  try:
    return file.write(towrite)
  except:
    error("FileOperationError", 0,f"{name}({towrite})", f"File with mode '{file.mode}' is not writable.")


@Aardvark.method("file", "read")
def read_file(name, file):
    try:
        return file.read()
    except:
        error("FileOperationError", 0,f"{name}()", f"File with mode '{file.mode}' is not readable.")
def getname(file):
  return file.name
