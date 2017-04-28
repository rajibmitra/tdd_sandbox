import pytest
import json
from fib import app


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
