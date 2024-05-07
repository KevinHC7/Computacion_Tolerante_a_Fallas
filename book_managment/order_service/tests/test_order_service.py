import pytest
import requests

def test_get_orders():
    response = requests.get('http://localhost:5003/orders')
    assert response.status_code == 200
    assert response.json() == []

def test_add_order():
    order_data = {'customer': 'Customer 1', 'book': 'Book 1', 'quantity': 1}
    response = requests.post('http://localhost:5003/orders', json=order_data)
    assert response.status_code == 200
    assert response.json() == {'message': 'Order added successfully!'}
