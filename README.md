# 🏎️ Formula Student Telemetry Dashboard

A Flask-based telemetry dashboard project for Formula Student vehicle monitoring.  
It visualizes live speed (from RPM), battery status, brake pressure, and temperature with warning indicators.

---

# 📖 Overview

This project simulates an automotive telemetry monitoring workflow using Flask and Python.  
It reads telemetry-style data from a CSV source and serves a real-time dashboard UI for vehicle diagnostics and monitoring.

The frontend fetches telemetry data from the backend every 5 seconds and dynamically updates live vehicle parameters.

---

# 📂 Current Repository Layout

```text
formula-student-telemetry-dashboard/
├── README.md
└── Downloads/dashboard_code/dashboard_code/
    ├── app.py
    ├── app2.py
    ├── excelreadcode.py
    ├── rpmlive.csv
    ├── templates/
    │   └── index.html
    ├── static/
    │   ├── style.css
    │   └── images/
    ├── package.json
    └── package-lock.json
```

---

# ✨ Features

- 🔄 Live dashboard updates every 5 seconds
- 🚗 RPM-based speed visualization
- 🔋 Battery SOC and telemetry monitoring
- 🛑 Brake pressure display
- 🌡️ Temperature display with warning threshold
- ⚙️ Flask backend API for telemetry data
- 🐍 Python-based telemetry validation workflow
- 📊 Lightweight automotive dashboard interface

---

# 🛠️ Tech Stack

### 💻 Software
- Python 3
- Flask
- HTML/CSS/JavaScript

### 🔌 Embedded & Telemetry Concepts
- ESP32 telemetry workflow concepts
- CAN communication workflow concepts
- RS-485 communication workflow concepts

### 📈 Data Handling
- CSV-based telemetry simulation

---

# 🚀 Getting Started

## 1️⃣ Clone the repository

```bash
git clone https://github.com/VishwajitChavan17/formula-student-telemetry-dashboard.git
cd formula-student-telemetry-dashboard/Downloads/dashboard_code/dashboard_code
```

---

## 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

---

## 3️⃣ Activate the environment

### 🪟 Windows (PowerShell)

```bash
.venv\Scripts\Activate.ps1
```

### 🍎🐧 Linux/macOS

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install dependency

```bash
pip install flask
```

---

## 5️⃣ Configure CSV path

In `app.py`, update:

```python
csv_file_path = 'D:/Dashboard Team Acc Html/car dashboard/rpmlive.csv'
```

to your local file path (example):

```python
csv_file_path = 'rpmlive.csv'
```

---

## 6️⃣ Run the app

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

# 🔗 API

## GET `/sensor-data`

### Example response

```json
{
  "speed": 3120,
  "battery": 75,
  "brake_pressure": 100,
  "temperature": 30
}
```

---

# 📝 Notes

- 📄 The current implementation uses CSV as telemetry input.
- ⚙️ `package.json` exists, but the running backend is Flask/Python.
- 🔒 Hardware-side integrations and Formula Student vehicle implementation details are excluded due to team confidentiality and proprietary design restrictions.
- 🔌 CAN/RS-485 live telemetry integration can be extended in future versions.

---

# 🚧 Future Improvements

- 🔗 Direct CAN telemetry ingestion
- 📡 Real-time serial communication support
- ⚡ WebSocket live stream updates
- 🚨 Configurable telemetry alerts and thresholds
- 🧠 Embedded diagnostics and fault monitoring
- 📊 Data logging and analytics pipeline

---

# 👨‍💻 Author

**Vishwajit Chavan**
