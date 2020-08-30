import flask
from Aardvark import *
#Aardvark.library
app = flask.Flask(__name__)


@Aardvark.function('render_string')
def render_string(name, msg, slug): #retruns a string
    @app.route(f'/{slug}')
    def index():
        return f'{msg}'


@Aardvark.function('run_server')
def run_server(name, ip='0.0.0.0', port=8080, debug=False):# Runs the server, app.run
    app.run(ip, port, debug=debug)


@Aardvark.function('render_file')
def render_file(name, src, slug): #Reder_template
    @app.route(f'/{slug}')
    def html():
        return flask.render_template_string(open(src).read())

@Aardvark.function('getrequest')
def getrequest(name): #Gets flasks request
  return flask.request
#These are the functions, you can see them being used in server_example.adk
#Are you here?
#yes