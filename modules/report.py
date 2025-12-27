"""
report.py
---------

Generates an organized stock trend report.

Responsibilities:
- Format trend analysis data into readable terminal reports.
- Include confidence, signal strength, volatility, and risk metrics.
- Optional: include ASCII/visual chart summaries.
"""

def format_report(ticker, df, analysis):
    last_close = df['Close'].iloc[-1]
    start_date = df.index[0].strftime('%Y-%m-%d')
    end_date = df.index[-1].strftime('%Y-%m-%d')

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("STOCK TREND REPORT")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    print(f"Stock: {ticker}")
    print(f"Last Close Price: ${last_close:.2f}")
    print(f"Data Range: {start_date} – {end_date}\n")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("TREND SUMMARY")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    print(f"Overall Trend: {analysis['Overall Trend']}")
    print(f"Confidence: {analysis['Confidence']}%")
    print(f"Signal Strength: {analysis['Signal Strength']}/100\n")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("SUPPORTING METRICS")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    print(f"Volatility (20-day): {analysis['Volatility']:.4f}")
    print(f"Max Drawdown: {analysis['Drawdown']:.2%}")
    print(f"Crossover Signal: {analysis['Crossover Signal']}\n")


    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("INTERPRETATION")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    if analysis['Confidence'] >= 70:
        print("• Strong agreement based on indicators.")
    elif analysis['Confidence'] >= 50:
        print("• Moderate signal alignment; trend may be developing.")
    else:
        print("• Mixed or weak signals; uncertain about market direction.")

    if analysis['Volatility'] > df['Volatility'].mean() * 1.5:
        print("• High volatility reflects a higher risk.")

    if analysis['Drawdown'] < -0.1:
        print("• Recent drawdown indicates downside pressure.\n")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("DISCLAIMER")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print("This tool provides probabilistic trend insights based on historical data.")
    print("It does NOT predict exact stock prices and should not be used as financial advice.\n")


    

