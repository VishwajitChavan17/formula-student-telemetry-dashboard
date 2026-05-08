import serial
import csv
import time

# Set up serial connection
arduino_port = "COM11"  # Change this to match your Arduino's COM port
baud_rate = 9600
timeout = 1

# Open a connection to the Arduino
try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=timeout)
    print(f"Connected to Arduino on {arduino_port} at {baud_rate} baud.")
    time.sleep(2)  # Give time for Arduino to reset
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit()

# Path to the CSV file where data will be saved
csv_file = "rpmlive.csv"

# Create/open the CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "RPM"])  # Write header

def append_to_csv(rpm_value):
    current_time = time.strftime("%H:%M:%S", time.localtime())
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([current_time, rpm_value])
        print(f"Logged RPM: {rpm_value} at {current_time}")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").strip()
            if line.startswith("RPM:"):
                try:
                    rpm_value = int(float(line.split(":")[1].strip()))  # Get RPM value
                    append_to_csv(rpm_value)  # Save to CSV
                except ValueError as ve:
                    print(f"Error parsing RPM data: {ve}")
        time.sleep(1)  # Fetch every second
except KeyboardInterrupt:
    print("Program stopped.")

finally:
    ser.close()
