import flask
from fib import fib

app = flask.Flask('fib')
app.testing = True


@app.route('/')
def app_root():
    return flask.jsonify(message='welcome!'), 200


@app.route('/fib/<input_value>')
def get_fib(input_value):
    return flask.jsonify(value=fib(input_value)), 200
