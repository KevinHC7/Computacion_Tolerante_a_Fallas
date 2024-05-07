from flask import Flask, jsonify

app = Flask(__name__)

# Data for demonstration
authors = [{'id': 1, 'name': 'Author 1'}, {'id': 2, 'name': 'Author 2'}]

@app.route('/')
def index():
    return jsonify(message="Welcome to Author Management Microservice!")

@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify(authors)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
