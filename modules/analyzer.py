"""
analyzer.py
-----------

Functions to analyze stock trends.

Responsibilities:
- Determine short-, mid-, and long-term trend directions.
- Compute trend confidence and signal strength.
- Aggregate metrics for report generation.
"""

import pandas as pd
from .preprocessing import *

def analyze_stock(df): # analyze the metrics calculated in preprocessing.py; determines the trend of the stock.
    trend_basic = 0 # base trend
    trend_extended = 0 # base extended trend (after a more extensive comparison)
    confidence = 50  # base confidence
    signal_strength = 50  # base signal strength

    # short_trend = 0
    # mid_trend = 0
    # long_trend = 0
    # # +1 Bullish, -1 Bearish, 0 Neutral

    close_today = df['Close'].iloc[-1]
    short_ma_today = df['Short_MA'].iloc[-1]
    mid_ma_today = df['Mid_MA'].iloc[-1]
    long_ma_today = df['Long_MA'].iloc[-1]

    # basic trend determination
    if close_today > short_ma_today:
        trend_basic += 1
    elif close_today < short_ma_today:
        trend_basic -= 1
    else:
        trend_basic += 0
    
    # evaluate trend based on moving averages
    if short_ma_today > mid_ma_today > long_ma_today:
        trend_extended += 1
    elif short_ma_today < mid_ma_today < long_ma_today:
        trend_extended -= 1
    else:
        trend_extended += 0
    # determines the confidence and signal score based on both trends (i took a conservative approach)
    if trend_basic == 0 or trend_extended == 0:
        pass
    elif trend_basic == trend_extended: # if trends are the same confidence and signal strength are slightly increased
        confidence += 10
        signal_strength += 5
    elif trend_basic != trend_extended: # if trends are different confidence and signal score are decreased more
        confidence -= 20
        signal_strength -= 10

    # check volatility
    volatility = df['Volatility'].iloc[-1]
    volatility_threshold = df['Volatility'].mean() * 1.5 # threshold for high volatility

    if volatility > volatility_threshold:
        confidence -= 10
        signal_strength -= 5

    # check drawdowns
    drawdown = df['Drawdown'].iloc[-1]
    if drawdown < -0.1:  # more than 10% drawdown
        confidence -= 15
        signal_strength -= 5
    
    # check for any crossovers (compares the last two days moving averages)
    if df['Short_MA'].iloc[-2] < df['Mid_MA'].iloc[-2] and short_ma_today > mid_ma_today:
        crossover_signal = "Bullish"
    elif df['Short_MA'].iloc[-2] > df['Mid_MA'].iloc[-2] and short_ma_today < mid_ma_today:
        crossover_signal = "Bearish"
    else:
        crossover_signal = "Neutral"

    if crossover_signal == "Neutral" and trend_extended == "Neutral":
        pass
    elif crossover_signal == trend_extended:
        confidence += 10
        signal_strength += 10
    else: # could either penalize or leave unchanged, i chose to slightly penalize
        confidence -= 5
        signal_strength -= 2

    # keeps confidence and signal strength value between 0 and 100
    confidence = max(0, min(100, confidence))
    signal_strength = max(0, min(100, signal_strength))    

    if trend_extended > 0:
        trend = "Bullish"
    elif trend_extended < 0:
        trend = "Bearish"
    else:
        trend = "Neutral"

    return {
        'Volatility': volatility,
        'Drawdown': drawdown,
        'Crossover Signal': crossover_signal,
        'Overall Trend': trend,
        'Confidence': confidence,
        'Signal Strength': signal_strength,
    }
    