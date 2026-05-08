from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serves the HTML file

@app.route('/sensor-data', methods=['GET'])
def sensor_data():
    # Simulated sensor data for testing
    data = {
        "speed": random.uniform(0, 110),  # Simulated RPM
        "battery": random.uniform(0, 100),  # Simulated battery percentage
        "brake_pressure": random.uniform(0, 200),  # Simulated brake pressure in BAR
        "temperature": random.uniform(0, 100)  # Simulated temperature in °C
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
