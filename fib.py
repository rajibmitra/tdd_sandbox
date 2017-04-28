import flask


app = flask.Flask('fib')
app.testing = True


@app.route('/')
def app_root():
    return flask.jsonify(message='welcome!'), 200
