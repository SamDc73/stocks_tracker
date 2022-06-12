import yfinance as yf
from prettytable import PrettyTable, DOUBLE_BORDER
from sys import argv
from tqdm import tqdm

# check if a user passed a ticker name, if not use the config file
if len(argv) > 1:
    tickers = argv[1:]
else:
    tickers = open('tickersName').read().splitlines()

# Get the actual price of the stocks:
myTable = PrettyTable(["ticker", "Price", "Change"])
for ticker in tqdm(tickers, leave=False, ascii=' ='):
    # Get the current price
    ticker_yahoo = yf.Ticker(ticker)
    ticker_info = ticker_yahoo.info  # Attempt to make things faster
    last_quote = ticker_info['regularMarketPrice']

    # get the company full name based on the ticker
    company_name = ticker_info['longName']

    # Get the price change persentage
    previous_close = ticker_info['regularMarketPreviousClose']
    priceChange = round((last_quote - previous_close) / last_quote * 100, 3)

    # Change the color of the output based if the numbers are up or down
    if priceChange < 0:  # if they are down they will be colored red
        last_quote = "\033[1;31m%s\033[0m" % last_quote
        company_name = "\033[1;31m%s\033[0m" % company_name
        symbol = "\033[1;31m%s\033[0m" % '%'
        priceChange = "\033[1;31m%s\033[0m" % priceChange + symbol
    else:  # else it will be colored Green
        last_quote = "\033[1;32m%s\033[0m" % last_quote
        company_name = "\033[1;32m%s\033[0m" % company_name
        symbol = "\033[1;32m%s\033[0m" % '%'
        priceChange = "\033[1;32m%s\033[0m" % priceChange + symbol

    myTable.add_row([company_name, last_quote, priceChange])


myTable.set_style(DOUBLE_BORDER)  # Change the style of the board
print(myTable)
