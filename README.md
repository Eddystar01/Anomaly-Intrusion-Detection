# Anomaly-Based Intrusion Detection Simulation

## 📌 Project Overview

This project is a **CYB 313 (Simulation and Modelling)** coursework focused on **modelling intrusion detection using anomaly detection**.
The system simulates normal network traffic, introduces suspicious behavior, and detects intrusions using **threshold-based anomaly detection**.
The results are visualized using graphs for clear analysis.

---

## 🎯 Project Objective

The main objective of this project is to:

* Simulate normal network traffic
* Introduce anomalous behavior (suspicious ports)
* Detect anomalies using simple rules
* Visualize intrusion detection results

This project demonstrates how **anomaly-based Intrusion Detection Systems (IDS)** work in a controlled simulation environment.

---

## 🛠 Tools & Technologies

* **Python 3**
* **NumPy** – for traffic simulation
* **Matplotlib** – for visualization

---

## 📂 Project Structure

```
CYB-313-Anomaly-Intrusion-Detection/
│
├── anomaly_detection_simulation.py
├── graphs/
│   ├── graph_full_detection.png
|   ├── graph_normal_traffic.png
|   └── graph_port_activity.png
└── README.md
```

---

## ⚙️ How the Simulation Works

### 1️⃣ Normal Traffic Generation

* Network traffic is simulated using a normal (Gaussian) distribution.
* Traffic represents **packets per second** over time.

### 2️⃣ Port Activity Simulation

* Common service ports (80, 443, 22) represent normal behavior.
* Unusual ports (9999, 6666) represent suspicious activity.

### 3️⃣ Anomaly Detection

* **Traffic anomaly:** Traffic exceeding a defined threshold.
* **Port anomaly:** Traffic associated with suspicious ports.

### 4️⃣ Visualization

The graph displays:

* 🔵 Normal network traffic
* ⚫ Detection threshold
* 🔴 Traffic anomalies
* 🟢 Strange port activity

---

## ▶️ How to Run the Project

### Step 1: Install dependencies

```bash
pip install numpy matplotlib
```

### Step 2: Run the simulation

```bash
python anomaly_detection_simulation_colored.py
```

A graph showing detected anomalies will appear.

---

## 📊 Output

The output graph clearly shows:

* Normal traffic behavior
* Threshold line
* Detected intrusions using different colors

This visualization supports analysis and defense of the simulation model.

---

## 📘 Academic Relevance

* Course: **CYB 313 – Simulation and Modelling**
* Topic: **Anomaly-Based Intrusion Detection**
* Method: **Simulation using artificial data**
* Suitable for:

  * Coursework submission
  * Project defense
  * Demonstration of IDS concepts

---

## ⚠️ Notes

* The data used is **simulated**, not real network traffic.
* Threshold values can be adjusted to observe different detection behaviors.
* Traffic-based attack spikes were commented out to focus on **port-based anomalies**.

---

## 👤 Author

**Olanrewaju Olamide E.**
Department of Cybersecurity
LAUTECH

---

## ✅ Conclusion

This project successfully models an anomaly-based intrusion detection system using simulation techniques. It provides a clear and simple demonstration of how abnormal network behavior can be detected and visualized using threshold-based rules.

---

**End of README**
