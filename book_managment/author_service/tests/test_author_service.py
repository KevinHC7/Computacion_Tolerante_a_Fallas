import pytest
import requests

def test_get_authors():
    response = requests.get('http://localhost:5001/authors')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'Author 1'}, {'id': 2, 'name': 'Author 2'}]
