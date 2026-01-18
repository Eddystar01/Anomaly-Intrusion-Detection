import numpy as np
import matplotlib.pyplot as plt

# SIMULATION SETTINGS

np.random.seed(1)
TIME_POINTS = 200

NORMAL_MEAN = 50
NORMAL_STD = 5

TRAFFIC_THRESHOLD = 90
SUSPICIOUS_PORTS = [9999, 6666]

# GENERATING NORMAL TRAFFIC

traffic = np.random.normal(NORMAL_MEAN, NORMAL_STD, TIME_POINTS)

# normal service ports
ports = np.random.choice([80, 443, 22], size=TIME_POINTS)

# INSERT ANOMALIES FOR TESTING

# traffic-based attacks
# traffic[40] = 130
# traffic[100] = 150
# traffic[160] = 170

# port-based attacks
ports[70] = 9999
ports[140] = 6666

# DETECTION

traffic_attack = traffic > TRAFFIC_THRESHOLD
port_attack = np.isin(ports, SUSPICIOUS_PORTS)

# classify attack types
traffic_indices = np.where(traffic_attack)[0]
port_indices = np.where(port_attack)[0]

# VISUALIZATION

plt.figure(figsize=(10, 5))

# normal traffic
plt.plot(traffic, label="Network Traffic", color="blue")

# threshold
plt.axhline(
    TRAFFIC_THRESHOLD,
    linestyle="--",
    color="black",
    label="Threshold"
)

# traffic-based attacks
plt.scatter(
    traffic_indices,
    traffic[traffic_indices],
    color="red",
    label="Traffic Anomaly"
)

# port-based attacks
plt.scatter(
    port_indices,
    traffic[port_indices],
    color="green",
    label="Strange Port Activity"
)

plt.title("Anomaly-Based Intrusion Detection Simulation")
plt.xlabel("Time")
plt.ylabel("Packets per Second")
plt.legend()
plt.show()