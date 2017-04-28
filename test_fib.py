import pytest
import json
from fib import app

# Acceptance tests
def test_app_root_answers_200_ok():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_app_root_gives_json_welcome_message():
    client = app.test_client()
    response = client.get('/')
    response_dict = json.loads(response.data)
    assert 'message' in response_dict
    assert 'welcome' in response_dict['message']
