from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def generate_store_data(num_stores=100):
    stores = []
    for i in range(1, num_stores + 1):
        store_name = f"Store {i}"
        revenue = random.randint(50000, 500000)
        stores.append({"name": store_name, "revenue": revenue})
    return stores

store_data = generate_store_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/revenue')
def get_revenue_data():
    search_term = request.args.get('search', '').lower()
    sort_by = request.args.get('sort_by', 'name')
    sort_order = request.args.get('sort_order', 'asc')

    filtered_stores = store_data
    if search_term:
        filtered_stores = [store for store in filtered_stores if search_term in store['name'].lower()]

    if sort_by == 'revenue':
        filtered_stores.sort(key=lambda x: x['revenue'], reverse=(sort_order == 'desc'))
    else:
        filtered_stores.sort(key=lambda x: x['name'], reverse=(sort_order == 'desc'))

    return jsonify(filtered_stores)

if __name__ == '__main__':
    app.run(debug=True)