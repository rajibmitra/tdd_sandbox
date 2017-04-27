import pytest
import flask


app = flask.Flask('fib')
app.testing = True


@app.route('/')
def fib_root():
    return '', 200


# Acceptance tests
def test_fib_rest_answers_200_ok():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
