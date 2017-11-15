#how to run
#go to command line
#set FLASK_APP=cifarrestapi.py
#set FLASK_DEBUG=1
#flask run

import flask

app= flask.Flask(__name__)

@app.route('/')
def index():
    '''default page'''
    return 'Index Page'


@app.route("/hello")
def hello():
    '''
    prints hello world
    '''
    return "Hello World!"

