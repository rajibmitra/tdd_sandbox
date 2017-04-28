import flask
from fib import fib

app = flask.Flask('fib')
app.testing = True


@app.route('/')
def app_root():
    return flask.jsonify(message='welcome!'), 200


@app.route('/fib/<input_value>')
def get_fib(input_value):
    try:
        value = fib(input_value)
    except ValueError:
        return flask.jsonify(message='Value must be an integer'), 400
    return flask.jsonify(value=value), 200
