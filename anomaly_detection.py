from collections import deque
import numpy as np

def z_score_anomaly_detection(data_stream, window_size=50, threshold=3):
    data_window = deque(maxlen=window_size)
    anomalies = []

    for data_point in data_stream:
        if len(data_window) == window_size:
            mean = np.mean(data_window)
            std = np.std(data_window)
            z_score = (data_point - mean) / std if std != 0 else 0

            if abs(z_score) > threshold:
                print(f"Anomaly detected: {data_point} (Z-score: {z_score})")
                anomalies.append(data_point)

        data_window.append(data_point)
        yield data_point, anomalies