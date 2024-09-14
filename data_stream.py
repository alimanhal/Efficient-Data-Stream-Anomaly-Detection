import requests
import time

API_KEY = 'your_alpha_vantage_api_key'
STOCK_SYMBOL = 'AAPL'
API_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}'

def fetch_stock_data():
    """
    Fetches real-time stock prices from Alpha Vantage API.

    Returns:
        list: A list of stock prices (float) for the last 100 minutes.
    """
    try:
        response = requests.get(API_URL) 
        if response.status_code == 200:
             data = response.json()
             time_series = data.get('Time Series (1min)', {})
        
             if not time_series:
                 raise ValueError("No data found in response.")
        
             stock_prices = [float(value['4. close']) for key, value in sorted(time_series.items())]
             return stock_prices
        elif response.status_code == 429:  # Rate limit hit
             print("API rate limit reached. Retrying in 30 seconds.")
             time.sleep(30)
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return []

def generate_data_stream():
    """
    Generates a continuous data stream using real-time stock prices.
    
    Yields:
        float: Stock price from the data stream.
    """
    while True:
        stock_data = fetch_stock_data()
        for price in stock_data:
            yield price
        time.sleep(30)  # Fetch data every minute