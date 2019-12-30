import yfinance as yf

data = yf.download('ITC', start="2017-04-01", end="2019-04-30")

data.head()

data.sample()