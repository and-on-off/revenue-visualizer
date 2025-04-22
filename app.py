from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Our sample data
store_data = {
    'labels': ['January', 'February', 'March', 'April'],
    'datasets': [
        {'label': 'Store A', 'data': [150000, 180000, 220000, 200000], 'backgroundColor': 'rgba(255, 99, 132, 0.7)', 'borderColor': 'rgba(255, 99, 132, 1)', 'borderWidth': 1},
        {'label': 'Store B', 'data': [250000, 280000, 310000, 300000], 'backgroundColor': 'rgba(54, 162, 235, 0.7)', 'borderColor': 'rgba(54, 162, 235, 1)', 'borderWidth': 1},
        {'label': 'Store C', 'data': [120000, 140000, 160000, 150000], 'backgroundColor': 'rgba(255, 206, 86, 0.7)', 'borderColor': 'rgba(255, 206, 86, 1)', 'borderWidth': 1}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/revenue')
def get_revenue_data():
    return jsonify(store_data)

if __name__ == '__main__':
    app.run(debug=True)