import matplotlib.pyplot as plt

def real_time_plot(data_points, anomalies):
    plt.ion()  # Enable interactive mode
    plt.clf()  # Clear the current plot
    
    # Plot the data stream as a line
    plt.plot(data_points, label='Data Stream')

    # Plot anomalies as red dots using scatter
    if anomalies:
        anomaly_indices = [i for i in range(len(data_points)) if data_points[i] in anomalies]
        plt.scatter(anomaly_indices, [data_points[i] for i in anomaly_indices], color='red', label='Anomalies', marker='o')
    
    # Add labels and legends
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    
    # Redraw the plot
    plt.draw()
    plt.pause(0.01)  # Short pause to update the plot