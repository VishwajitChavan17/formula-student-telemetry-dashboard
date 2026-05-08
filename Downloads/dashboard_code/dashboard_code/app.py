from flask import Flask, jsonify, render_template
import csv
import os

app = Flask(__name__)

# Path to the CSV file
csv_file_path = 'D:/Dashboard Team Acc Html/car dashboard/rpmlive.csv'

# Function to read the latest RPM value from the CSV
def read_latest_rpm():
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1:
                latest_row = data[-1]  # Get the latest row of data
                rpm = int(float(latest_row[1]))  # Assuming RPM is in the second column
                print(f"Latest RPM read from CSV: {rpm}")  # Debugging statement
                return rpm
            else:
                print("No data found in CSV.")
                return 0
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return 0

# Route for the main dashboard page
@app.route('/')
def dashboard():
    return render_template('index.html')  # Ensure 'index.html' is in the templates folder

# Route to provide the latest RPM data as JSON for the frontend to fetch
@app.route('/sensor-data')
def sensor_data():
    rpm = read_latest_rpm()
    sensor_data = {
        'speed': rpm,  # assuming RPM data is directly used as speed in the dashboard
        'battery': 75,  # Placeholder values for other data
        'brake_pressure': 100,
        'temperature': 30
    }
    return jsonify(sensor_data)

if __name__ == '__main__':
    # Check if CSV file path exists
    if os.path.exists(csv_file_path):
        print(f"CSV file found at {csv_file_path}. Starting Flask app...")
    else:
        print(f"CSV file not found at {csv_file_path}. Please check the file path.")
    app.run(debug=True)
