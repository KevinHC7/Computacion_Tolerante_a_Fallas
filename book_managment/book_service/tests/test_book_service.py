import pytest
import requests

def test_get_books():
    response = requests.get('http://localhost:5000/books')
    assert response.status_code == 200
    assert response.json() == []

def test_add_book():
    book_data = {'title': 'Book 1', 'author': 'Author 1', 'isbn': '1234567890'}
    response = requests.post('http://localhost:5000/books', json=book_data)
    assert response.status_code == 200
    assert response.json() == {'message': 'Book added successfully!'}
