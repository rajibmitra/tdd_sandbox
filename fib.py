import flask


app = flask.Flask('fib')
app.testing = True


@app.route('/')
def fib_root():
    return '', 200
