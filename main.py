import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import pandas_datareader.data as web
#---------------
def get_close_date(pd,date):
    while (1):
        date_close = pd.loc[pd['Date']==date]
        if (date_close.empty)==False:
            return date_close
        date+=1
        
def plot(minimum,length,new_df_ohlc,num=365):
    total=[]
    special_date=[0,91,182,242]
    special_date_2=[121,274]
        
    for k in range(num):
            
        analysis = pd.DataFrame()
        start=minimum+k
        print(k)
        for i in range(length-362):
            j=i%365
            
            now=start+i

            if j in special_date:
                if k==364:
                    ax1.axvline(x=now,color='b',linewidth=0.5)
                date_close = get_close_date(new_df_ohlc,now)
                analysis = pd.concat([analysis,date_close])
            elif j in special_date_2:
                if k==364:
                    ax1.axvline(x=now,color='r',linewidth=0.5)
                date_close = get_close_date(new_df_ohlc,now)
                analysis = pd.concat([analysis,date_close])

                
        close = analysis.filter(['Close'])
        date = analysis.filter(['Date'])
        analysis['close_shift']=(close-close.shift(1))/close.shift(1)
        analysis['date_shift']=date-date.shift(1)
        analysis['slope']=((1+analysis['close_shift'])**(1/analysis['date_shift'])-1)*100
        analysis['abs_slope'] = abs(analysis['slope'])
        temp_point=[0,0]
        for index, row in analysis.iterrows():
            if temp_point!=[0,0]:
                if k==364:
                    ax1.plot([temp_point[0],row['Date']], [temp_point[1],row['Close']],'black',linewidth=1)
                temp_point=[row['Date'],row['Close']]
            else:
                temp_point=[row['Date'],row['Close']]
        #ax1.plot([734000,734091], [18,30],'m-',linewidth=1)
        total.append(analysis['abs_slope'].sum())

    total = np.array(total)
    sort_index = np.argsort(total)
    #print(total)
    sort_index_reverse=sort_index[::-1]
    cycle_max_relationship=sort_index_reverse[0]
    #print(cycle_max_relationship)
    return cycle_max_relationship,-np.sort(-total)

import os
import csv

style.use('ggplot')
directory = 'stock_dfs/'
file_list=[]
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_list.append(filename)

stock_date_pair=[]
array_pair=[]
for file in file_list:
    print(file)
    df = pd.read_csv('stock_dfs/'+file, parse_dates=True, index_col=0)
    
    new_df_ohlc=df[['Open','High','Low','Close','Volume']]
    new_df_ohlc.reset_index(inplace=True)
    new_df_ohlc['Date'] = new_df_ohlc.index
    df_volume = new_df_ohlc['Volume']



    minimum=new_df_ohlc.iloc[0]['Date']
    maximum=new_df_ohlc.iloc[-1]['Date']
    length = int(maximum-minimum)

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)


    candlestick_ohlc(ax1, new_df_ohlc.values, colorup='g')
    ax2.fill_between(df_volume.index, df_volume.values, 0)
    cycle_date,array = plot(minimum,length,new_df_ohlc)
    print(cycle_date)
    print(array)
    stock_date_pair.append(cycle_date)
    array_pair.append(array)

    with open('output.csv', 'w+', newline='') as csvfile:
      # 建立 CSV 檔寫入器
      writer = csv.writer(csvfile)

      writer.writerow(['ticker', 'cycle_date'])
      for i in range(len(stock_date_pair)):
          writer.writerow([file_list[i],stock_date_pair[i], array_pair[i]])

    

#---------------------
plt.show()
