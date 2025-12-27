"""
visualizer.py
-------------

FOR FUTURE IMPLEMENTATION:
Creates visual summaries of stock data.
"""

import matplotlib.pyplot as plt
# import mplfinance as mpf // for later charts

def plot_moving_averages(df, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(df.index, df['Close'], label='Closing Price', linewidth = 2, color='black') 
    plt.plot(df.index, df['Short_MA'], label='5-Day MA', linewidth = 1.5, color='red')
    plt.plot(df.index, df['Mid_MA'], label='20-Day MA', linewidth = 1.5, color='orange')
    plt.plot(df.index, df['Long_MA'], label='100-Day MA', linewidth = 1.5, color='yellow')  

    plt.title(f'{ticker} Closing Price with 5, 20, and 100 Day Moving Averages')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_volatility(df, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(df.index, df['Close'], label='Closing Price', linewidth=2, color='black')
    plt.fill_between(df.index, df['Close'] - df['Volatility'], df['Close'] + df['Volatility'], color='red', alpha=0.2)

    plt.title(f'{ticker} Closing Price with Volatility')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.tight_layout() 
    plt.show()

def plot_volume(df, ticker):
    plt.figure(figsize=(12,6))

    colors = ['green' if df['Close'].iloc[i] >= df['Close'].iloc[i-1] else 'red' for i in range(1, len(df))]
    plt.bar(df.index[1:], df['Volume'][1:], color=colors, alpha=0.6)

    plt.title(f"{ticker} Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")

    plt.tight_layout()
    plt.show()

def display_charts(df, ticker):
    plot_moving_averages(df, ticker)
    plot_volatility(df, ticker)
    plot_volume(df, ticker)
