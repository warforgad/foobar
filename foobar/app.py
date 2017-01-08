from flask import Flask
from . import foo, bar
my_app = Flask(__name__)

@my_app.route('/foo')
def get_foo():
    return foo()

@my_app.route('/bar')
def get_bar():
    return bar()
