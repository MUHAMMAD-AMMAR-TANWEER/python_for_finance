import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

df = pd.read_csv('google.csv', parse_dates=True , index_col=0)
print(df.head())

#This is for ploting good graphg

#df["Adj Close"].plot()
df.plot()
plt.show()