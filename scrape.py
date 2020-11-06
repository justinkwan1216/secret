import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import pandas_datareader.data as web
file = "output2.csv"
df = pd.read_csv(file, parse_dates=True, index_col=0)
print((df[(df['current_price'] < 10) & (df['ATR_2'] < 0.001)]).to_string())
