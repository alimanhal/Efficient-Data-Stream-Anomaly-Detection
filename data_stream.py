import numpy as np
import random

def generate_data_stream():
    t = 0
    while True:
        seasonal = 10 * np.sin(0.1 * t)
        noise = random.uniform(-1, 1)
        anomaly = random.uniform(10, 20) if random.random() < 0.05 else 0
        yield seasonal + noise + anomaly
        t += 1
