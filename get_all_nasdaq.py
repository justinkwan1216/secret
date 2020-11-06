import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from ta.volatility import AverageTrueRange

def save_all_nasdaq_tickers():
    df = pd.read_csv('NASDAQ.csv')
    tickers = df['Symbol'].values
    #for each in tickers:
    #    print(each)
    with open("nasdaqtickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    #return tickers

save_all_nasdaq_tickers()
# save_sp500_tickers()
import yfinance as yf

def get_data_from_yahoo(reload_nasdaq=False):
    if reload_nasdaq:
        tickers = save_nasdaq_tickers()
    else:
        with open("nasdaqtickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stock_nasdaq'):
        os.makedirs('stock_nasdaq')

    start = dt.datetime(2019, 1, 1)
    end = dt.datetime.now()
    
    for ticker in tickers:
        print(ticker)
        ticker = ticker.strip("\n")
        if "." in ticker:
            ticker = ticker.replace(".","-")
        #print(ticker)
        # just in case your connection breaks, we'd like to save our progress!
        if not os.path.exists('stock_nasdaq/{}.csv'.format(ticker)):
            try:
                #df = web.DataReader(ticker, 'yahoo', start, end)
                #iex-tops econdb
                #df.reset_index(inplace=True)
                #df.set_index("Date", inplace=True)

                #df = df.drop("Symbol", axis=1)
                df = yf.download(ticker,start=start,end=end)
                # Initialize ATR Indicator
                indicator_atr = AverageTrueRange(high=df["High"],low=df["Low"],close=df["Close"])

                # Add ATR
                df['ATR'] = indicator_atr.average_true_range()

                # Initialize ATR Indicator
                indicator_atr_2 = AverageTrueRange(high=df["ATR"],low=df["ATR"],close=df["ATR"])

                # Add ATR
                df['ATR_2'] = indicator_atr_2.average_true_range()
                
                df.to_csv('stock_nasdaq/{}.csv'.format(ticker))

            except:
                continue
            
        else:
            print('Already have {}'.format(ticker))


get_data_from_yahoo()
def compile_data():
    with open("nasdaqtickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        ticker = ticker.strip("\n")
        if "." in ticker:
            ticker = ticker.replace(".","-")
        df = pd.read_csv('stock_nasdaq/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
    print(main_df.head())
    main_df.to_csv('nasdaq_joined_closes.csv')
#compile_data()
def visualize_data():
    df = pd.read_csv('nasdaq_joined_closes.csv')
    df_corr = df.corr()
    print(df_corr.head())
    df_corr.to_csv('nasdaqcorr.csv')
    data1 = df_corr.values
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
    fig1.colorbar(heatmap1)

    ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
    ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)
    ax1.invert_yaxis()
    ax1.xaxis.tick_top()
    column_labels = df_corr.columns
    row_labels = df_corr.index
    ax1.set_xticklabels(column_labels,fontsize=1)
    ax1.set_yticklabels(row_labels,fontsize=1)
    ax1.xaxis.set_tick_params(labelsize=1)
    ax1.yaxis.set_tick_params(labelsize=1)
    plt.xticks(rotation=90)
    heatmap1.set_clim(-1, 1)
    #plt.tight_layout()
    #plt.show()
    plt.savefig('correlation.png',dpi=1000)
#visualize_data()
