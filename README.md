🏥 Real-Time Healthcare Monitoring Dashboard
This project is a real-time healthcare monitoring system that collects and visualizes vital sign data such as Heart Rate, Body Temperature, and SpO2 (Oxygen Saturation). Using MQTT for data streaming and machine learning for anomaly detection, it ensures early detection of potential health risks.

🌟 Key Features
Real-Time Monitoring: The system fetches live health data from sensors via MQTT and displays it on a Streamlit-based dashboard.

Anomaly Detection: Using a pre-trained Isolation Forest model, the system flags any anomalies in the vital signs.

Alert System: Displays alerts in case abnormal data is detected (e.g., Heart Rate > 100 bpm).

Visualization: Dynamic charts show the latest data trends for better insights.

⚙️ Technologies Used
Python: Programming language used to build the dashboard and train the model.

Streamlit: Interactive web app framework for creating the dashboard.

MQTT: Lightweight messaging protocol for real-time data streaming.

scikit-learn: Used for training the anomaly detection model (Isolation Forest).

pandas: Data manipulation and storage in CSV format.

pickle: Model serialization for saving and loading the trained anomaly detection model.

JSON: Data format for transmitting sensor data
