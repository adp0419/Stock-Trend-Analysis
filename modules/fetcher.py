"""
fetcher.py
-----------

Functions for fetching historical stock data from Yahoo Finance.

Responsibilities:
- Connect to Yahoo Finance using yfinance.
- Retrieve stock price data for a given ticker.
- Return data in a format ready for preprocessing and analysis.
"""

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

import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(ticker, start_date = "2018-01-01", end_date = None):
    if end_date is None:
        end_date = datetime.today().strftime('%Y-%m-%d') # Sets today as default end date

    stock = yf.Ticker(ticker)

    df = stock.history(start = start_date, end = end_date)

    if df.empty:
        raise ValueError(f'No data found for ticker: {ticker}')
    
    return df