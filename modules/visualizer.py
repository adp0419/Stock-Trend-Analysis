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
