import pytest

from fib import app

# Acceptance tests
def test_fib_rest_answers_200_ok():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
