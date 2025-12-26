"""
main.py
--------

Main file of the project. Controls the flow of program, no logic is created here. 

Responsibilities:
- Display the menu, general information, and disclaimer.
- Accept user input for stock ticker symbols.
- Call functions from the modules to fetch data, analyze trends, generate reports, and display visuals.
- Handle user commands such as quitting or returning to the menu.
"""

from modules.fetcher import *
from modules.preprocessing import *
from modules.analyzer import *
from modules.report import *
from modules.visualizer import *

def menu():
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("📈 STOCK TREND ANALYSIS TOOL")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\nDisclaimer: This tool provides probabilistic trend insights based on historical data.")
    print("It does NOT predict exact stock prices and should not be used as financial advice.\n")

def main():
    while True:
        menu()
        ticker = input("Enter a stock ticker symbold (or 'Q' to quit): ").upper().strip()
        if ticker == 'Q':
            print("Exiting... Goodbye!")
            break
        else:
            print(f"\nFetching data for {ticker}...\n")

            # calling all functions made to fetch stock data, analyze it, and then format it
            df = fetch_stock_data(ticker)
            df = preprocess_data(df)
            analysis = analyze_stock(df)
            format_report(ticker, df, analysis)
            plot_moving_averages(df, ticker)

            end_choice = input("Enter 'C' to continue to menu or 'Q' to quit\n> ").upper().strip()

            if end_choice == "C":
                continue
            elif end_choice == "Q":
                print("Exiting... Goodbye!")
                break

if __name__ == "__main__":
    main()