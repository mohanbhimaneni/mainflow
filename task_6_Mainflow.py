import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/bhmoh/Downloads/disney_plus_titles.csv",parse_dates=True)
print(df.head())
print(df.isna().sum())
print(df.describe())
df=pd.DataFrame(df['release_year'])
print(df)
print(df.shape)
df['release_year'].plot(xlabel='No. of shows released',ylabel='Year of release')
plt.title('No. of shows released each year')
plt.show()
from statsmodels.tsa.filters.hp_filter import hpfilter
release_cycle, release_trend = hpfilter(df['release_year'], lamb=1200)
print(release_cycle)
print(release_trend)
df['Trend']=release_trend
df[['release_year', 'Trend']].plot().autoscale(axis='x', tight=True)
