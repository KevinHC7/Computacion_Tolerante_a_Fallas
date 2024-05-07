from flask import Flask, jsonify

app = Flask(__name__)

# Data for demonstration
inventory = [{'id': 1, 'name': 'Book 1', 'quantity': 10}, {'id': 2, 'name': 'Book 2', 'quantity': 5}]

@app.route('/')
def index():
    return jsonify(message="Welcome to Inventory Management Microservice!")

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
