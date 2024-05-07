import pytest
import requests

def test_get_inventory():
    response = requests.get('http://localhost:5002/inventory')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'Book 1', 'quantity': 10}, {'id': 2, 'name': 'Book 2', 'quantity': 5}]
