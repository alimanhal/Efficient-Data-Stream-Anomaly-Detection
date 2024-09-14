from data_stream import generate_data_stream
from anomaly_detection import z_score_anomaly_detection
from visualization import real_time_plot

def main():
    """
    Main function to run the anomaly detection process using real-time stock prices.
    """
    data_stream = generate_data_stream()  # Using the real-time stock price stream
    data_points = []
    all_anomalies = []

    # Set window size and threshold for anomaly detection
    window_size = 50
    threshold = 3

    # Call the anomaly detection function with real-time stock data
    detection = z_score_anomaly_detection(data_stream, window_size, threshold)

    for data_point, anomalies in detection:
        data_points.append(data_point)
        all_anomalies.extend(anomalies)

        # Update plot every 10 data points
        if len(data_points) % 10 == 0:
            real_time_plot(data_points, all_anomalies)

if __name__ == "__main__":
    main()
