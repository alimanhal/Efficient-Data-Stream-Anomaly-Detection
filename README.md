# Efficient Data Stream Anomaly Detection

This project implements an anomaly detection system using Python, real-time financial data, and a Z-score-based algorithm to identify anomalies. The anomalies are detected and plotted dynamically in real-time with continuous stock price streams from Yahoo Finance.

## Project Overview
The objective of this project is to detect unusual patterns in a continuous data stream that represents stock prices. The script flags anomalies by identifying deviations from the norm in real-time, allowing for early detection of unusual behavior. 

- **Algorithm Used**: Z-score Anomaly Detection
- **Real-Time Data**: Stock price data stream from Yahoo Finance
- **Visualization**: Real-time plotting using `matplotlib`
- **Programming Language**: Python

## Key Features

- **Real-Time Data Stream**: Continuously fetches and processes stock data.
- **Anomaly Detection**: Uses the Z-score method to detect anomalies when the data points exceed a defined threshold.
- **Data Visualization**: Displays a real-time plot of the data stream and highlights anomalies with red dots.
- **Optimization**: Efficiently handles API rate limits and batch processing for smooth real-time detection.

## How It Works

The project is divided into four main components:

1. **Data Stream**: Uses Alpha Vantage API to fetch real-time stock data.
2. **Anomaly Detection**: Applies Z-score-based logic to flag anomalies.
3. **Visualization**: Generates real-time visualizations with anomalies marked.
4. **Error Handling**: Includes error handling for API limits and other issues.

![Graph Example] 
![image](https://github.com/user-attachments/assets/fc3e5fde-50a9-467e-a2b9-99b2605eb6ef)


### Example Output

Terminal showing detected anomalies:
```plaintext
Anomaly detected: 223.94000244140625 (Z-score: 3.185542874274288)
Anomaly detected: 223.1385040283203 (Z-score: -4.367154440057992)
Anomaly detected: 222.87860107421875 (Z-score: -3.431356428497915)
![image](https://github.com/user-attachments/assets/d0bd7f69-1dd4-4bf4-a317-ac467cc9a284)

