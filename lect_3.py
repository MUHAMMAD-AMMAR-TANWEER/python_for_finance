import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web

style.use('ggplot')

df = pd.read_csv('google.csv', parse_dates=True , index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100).mean() #100ma is previous 99 values + current value /100
#df.dropna(inplace=True)
df['100ma'] = df['Adj Close'].rolling(window=100 , min_periods=0).mean()# by this we Adj Close = 100 ma till 99 values

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)# for some cool visualization
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
print(df.head())