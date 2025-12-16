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
            
            # ----------------------------Temporary Try/Except--------------------------------- #
            try:
                df = fetch_stock_data(ticker)
                print(df.head())
            except Exception as e:
                print(f"Error fetching data: {e}")
            # -------------------------------------------------------------------------------- #

            end_choice = input("Enter 'C' to continue to menu or 'Q' to quit\n> ").upper().strip()

            if end_choice == "C":
                continue
            elif end_choice == "Q":
                print("Exiting... Goodbye!")
                break

if __name__ == "__main__":
    main()