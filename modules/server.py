import flask
import re
from Aardvark import *
#Aardvark.library
app = flask.Flask(__name__)
regex["isreturnhtml"] = re.compile('[\t ]*return html (.+)')

pages = {}
errorhandlers = {}

def returnhtml(toret, line_num):
    thing = Aardvark.gettype(toret, line_num)
    if thing[0] == "file":
        try:
            return thing[1].read()
        except:
            error(
                "FileModeError", line_num,
                f"return html open('{thing[1].name}', '{thing[1].mode}')",
                f"Unsuported mode for webpage '{thing[1].mode}', must be in a readable mode"
            )
    elif thing[0] == "string":
        return thing[1]
    else:
        error("TypeError", line_num, f"return html {thing[1]}",
              "Unsupported type for rendering html")


def webpage(code, line_num):
    code = code.split("\n")
    isweb = regex['iswebpage'].fullmatch(code[0])
    slug = Aardvark.gettype(isweb.groups()[0], line_num)
    if slug[0] != "string":
        error("TypeError", Aardvark.line_num, f"webpage {slug[1]} {{",
              'Route type must be string')
    else:
        exec(f"""@app.route('/{slug[1]}')
def website_{slug[1]}():  
  code=pages['{slug[1]}']
  global keywords
  keywords['isreturnhtml']=returnhtml
  for line in code[1:]:
    a=Aardvark.parse_line(line, Aardvark.line_num)
    if a!=None:
      return a
                  """)
        pages[slug[1]] = code


def errorhandler(code, line_num):
    code = code.split("\n")
    isweb = regex['iserrorhandler'].fullmatch(code[0])
    errorcode = Aardvark.gettype(isweb.groups()[0], line_num)
    if errorcode[0] != "number":
        error("TypeError", Aardvark.line_num, f"error {errorcode} {{",
              'Error code must be a number')
    else:
        exec(f"""@app.errorhandler({errorcode[1]})
def websiteerror_{errorcode[1]}(error):  
  code=errorhandlers[{errorcode[1]}]
  global keywords
  keywords['isreturnhtml']=returnhtml
  for line in code[1:]:
    a=Aardvark.parse_line(line, Aardvark.line_num)
    if a!=None:
      return a
                  """)
        errorhandlers[errorcode[1]] = code


@Aardvark.function('getrequest')
def getrequest(name):
    return flask.request


@Aardvark.function('run_server')
def run_server(name, ip='0.0.0.0', port=8080,
               debug=False):  # Runs the server, app.run
    app.run(ip, port, debug=debug)


regex["iswebpage"] = re.compile("[\t ]*webpage (.+?)[\t ]*{[\t ]*")
blocks["iswebpage"] = webpage
regex["iserrorhandler"] = re.compile("[\t ]*error (.+?)[\t ]*{[\t ]*")
blocks['iserrorhandler'] = errorhandler
