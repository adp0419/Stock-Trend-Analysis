"""
preprocessing.py
----------------

Functions for preparing stock data for analysis.

Responsibilities:
- Compute moving averages (short, mid, long-term).
- Calculate volatility metrics.
- Compute drawdowns and normalize features.
- Provide preprocessed data to the analyzer module.
"""

import pandas as pd
from modules.fetcher import fetch_stock_data

def compute_moving_averages(df, short_window = 5, mid_window = 20, long_window = 100): # Compute moving averages for 5, 20, & 100 day periods
    df['Short_MA'] = df['Close'].rolling(window = short_window).mean()
    df['Mid_MA'] = df['Close'].rolling(window = mid_window).mean()
    df['Long_MA'] = df['Close'].rolling(window = long_window).mean()
    return df

def compute_volatility(df, window = 20): # Computes volatility (standard deviation) over 20 day period
    df['Volatility'] = df['Close'].rolling(window = window).std()
    return df

def compute_drawdowns(df): # Computes drawdowns (% drop from a peak)
    df['Cumulative_Max'] = df['Close'].cummax()
    df['Drawdown'] = (df['Close'] - df['Cumulative_Max']) / df['Cumulative_Max']
    return df

def rescale_close(df): # Rescales the closing price to be between 0-1 (helps with comparing data)
    df['Rescaled_Close'] = (df['Close'] - df['Close'].min()) / (df['Close'].max() - df['Close'].min())
    return df