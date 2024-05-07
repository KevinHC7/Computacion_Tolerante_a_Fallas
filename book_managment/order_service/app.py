from flask import Flask, jsonify, request

app = Flask(__name__)

# Data for demonstration
orders = []

@app.route('/')
def index():
    return jsonify(message="Welcome to Order Management Microservice!")

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    orders.append(data)
    return jsonify(message="Order added successfully!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
