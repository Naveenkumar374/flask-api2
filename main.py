from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for the API
data = [
    {"SO_number": 101, "Item_name": "Item A", "Quantity": 10, "Price": 100.5, "Weight": 2.5},
    {"SO_number": 102, "Item_name": "Item B", "Quantity": 5, "Price": 50.0, "Weight": 1.2},
    {"SO_number": 103, "Item_name": "Item C", "Quantity": 20, "Price": 200.0, "Weight": 5.0}
]

# Route to get all data
@app.route('/geosoft/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)