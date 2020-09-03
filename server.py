import flask
from Aardvark import *
#Aardvark.library
app = flask.Flask(__name__)


@Aardvark.function('render_string')
def render_string(name, msg, slug=''): #retruns a string
    @app.route(f'/{slug}')
    def index():
        return f'{msg}'


@Aardvark.function('run_server')
def run_server(name, ip='0.0.0.0', port=8080, debug=False):# Runs the server, app.run
    app.run(ip, port, debug=debug)


@Aardvark.function('render_file')
def render_file(name, src, slug=''): #Render_template
    @app.route(f'/{slug}')
    def html():
        return flask.render_template_string(open(src).read())

@Aardvark.function('getrequest')
def getrequest(name): #Gets flasks request
  return flask.request

@Aardvark.function("errorhandler")
def handle_error(name, error, file):
  @app.errorhandler(error)
  def own_404_page(error):
    return render_file(file)