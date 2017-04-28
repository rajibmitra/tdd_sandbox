import pytest
import json
from flaskapp import app


@pytest.fixture
def client():
    return app.test_client()


# Acceptance tests
def test_app_root_answers_200_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_app_root_gives_json_welcome_message(client):
    response = client.get('/')
    response_dict = json.loads(response.data)
    assert 'message' in response_dict
    assert 'welcome' in response_dict['message']


def test_get_fib_0_returns_value_0(client):
    response = client.get('/fib/0')
    response_dict = json.loads(response.data)
    assert 'value' in response_dict
    assert response_dict['value'] == 0


def test_get_fib_8_returns_value_21(client):
    response = client.get('/fib/8')
    response_dict = json.loads(response.data)
    assert response_dict['value'] == 21


def test_post_to_fib_returns_405_not_allowed(client):
    response = client.post('/fib/0')
    assert response.status_code == 405


def test_get_fib_of_string_returns_400_bad_request(client):
    response = client.get('/fib/not_an_int')
    assert response.status_code == 400


def test_get_fib_of_float_returns_400_bad_request(client):
    response = client.get('/fib/4.5')
    assert response.status_code == 400
