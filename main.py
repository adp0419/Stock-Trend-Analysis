"""
main.py
--------

Entry point of the Stock Trend Analysis Tool.

Responsibilities:
- Display the menu, general information, and disclaimer.
- Accept user input for stock ticker symbols.
- Call functions from the modules to fetch data, analyze trends, generate reports, and display visuals.
- Handle user commands such as quitting or returning to the menu.

Note:
- Controls the flow of the program; does not implement analysis logic itself.
"""

from modules.fetcher import fetch_stock_data
from modules.analyzer import analyze_stock
from modules.report import format_report

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

            df = fetch_stock_data(ticker)
            # format_report(analyze_stock(df))


            end_choice = input("Enter 'C' to continue to menu or 'Q' to quit\n> ").upper().strip()

            if end_choice == "C":
                continue
            elif end_choice == "Q":
                print("Exiting... Goodbye!")
                break

if __name__ == "__main__":
    main()