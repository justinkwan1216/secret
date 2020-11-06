import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import pandas_datareader.data as web
df = pd.read_csv('nasdaq_output_all.xlsx', parse_dates=True, index_col=0)
print(df)
