# engine/data_utils.py
import pandas as pd
import numpy as np

# Sample Data from the assignment [cite: 129-132]
SAMPLE_DATA = """
date, open, high, low, close, volume
2023-01-01, 100, 105, 99, 103, 900000
2023-01-02, 103, 108, 101, 107, 1200000
2023-01-03, 107, 110, 106, 109, 1300000
2023-01-04, 109, 112, 108, 110, 1150000
2023-01-05, 110, 113, 109, 112, 1400000
2023-01-06, 112, 115, 111, 114, 1500000
2023-01-07, 114, 117, 113, 115, 1350000
2023-01-08, 115, 118, 114, 117, 1450000
2023-01-09, 117, 119, 116, 118, 1550000
2023-01-10, 118, 120, 117, 119, 1600000
2023-01-11, 119, 121, 118, 120, 1700000
2023-01-12, 120, 122, 119, 121, 1400000
2023-01-13, 121, 123, 120, 122, 1500000
2023-01-14, 122, 124, 121, 123, 1600000
2023-01-15, 123, 125, 122, 124, 1700000
2023-01-16, 124, 126, 123, 125, 1800000
2023-01-17, 125, 127, 124, 126, 1900000
2023-01-18, 126, 128, 125, 127, 2000000
2023-01-19, 127, 129, 126, 128, 1850000
2023-01-20, 128, 130, 127, 129, 1950000
2023-01-21, 129, 131, 128, 130, 2100000
2023-01-22, 130, 132, 129, 128, 900000
2023-01-23, 128, 131, 127, 129, 950000
2023-01-24, 129, 133, 128, 132, 2200000
2023-01-25, 132, 135, 131, 134, 2300000
"""
# ... add more synthetic data here for meaningful backtest results ...

def load_data():
    df = pd.read_csv(pd.io.common.StringIO(SAMPLE_DATA), parse_dates=['date']).set_index('date')
    df.columns = [col.strip().upper() for col in df.columns] # Normalize column names (strip whitespace and uppercase)
    return df

def calculate_sma(series, period):
    # This is a helper for the CODE GENERATOR to use.
    return series.rolling(period).mean()

# Add a placeholder for RSI calculation...
# def calculate_rsi(series, period):
#     ...