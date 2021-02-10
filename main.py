import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf

import datetime as dt

crypto_1 = "BTC"
crypto_2 = "ETH"
fiat_1 = "USD"
fiat_2 = "EUR"

start = dt.datetime(2020, 12, 1)
end = dt.datetime.now()

btc = web.DataReader(f"{crypto_1}-{fiat_1}", "yahoo", start, end)
eth = web.DataReader(f"{crypto_2}-{fiat_2}", "yahoo", start, end)

mpf.plot(btc, type="candle", volume=True, style="yahoo")

plt.yscale("log")

plt.plot(btc['Close'], label="BTC")
plt.plot(eth['Close'], label="ETH")
plt.legend(loc="upper left")
plt.show()
