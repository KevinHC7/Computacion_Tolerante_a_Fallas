from flask import Flask, jsonify

app = Flask(__name__)

# Data for demonstration
books = []

@app.route('/')
def index():
    return jsonify(message="Welcome to Book Management Microservice!")

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return jsonify(message="Book added successfully!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
