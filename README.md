# prerequisite
you need to get couple of packages first by runnign : \
`pip install --use yfinance prettytable tqdm`

# Used modules
- [YFinance](https://github.com/ranaroussi/yfinance): to get stocks prices :)
- sys(argv): to enter the stock name
- [PrettyTable](https://github.com/jazzband/prettytable): to print the data in a table
- [tqdm](https://github.com/tqdm/tqdm): get a progrss ba

# How to use it : 
you can simply run by typing `python stocks.py` in you terminal \
by doing so the app will prase ticker from `tickersName` file.\
you can also pass a ticker to the app by : \
`python stocks.py AAPL`  \
or you can pass more than one ticker too: \
`python stocks.py AAPL GOOG IBM`

## tickersName (the config file)
you can add ticker to the tickerName file so you when you run `python stocks.py` it will get the ticker names from there. \
the file structe is very simple, one ticker per line (thats all )

