'''
Bureau of Labor Statistics - Unemployment Rate
[https://data.bls.gov/cgi-bin/surveymost?bls]
Unemployment Rate (Seasonally Adjusted) - LNS14000000
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = '/home/cgreco/Downloads/SeriesReport-20240716112125_2c4f30.xlsx'
df = pd.read_excel(filename, header = 11)   # row count begins with zero
#df = df.replace(np.nan,99)
#df.columns = range(1, 13)
df = df.rename(columns={'Jan':1,'Feb':2, 'Mar':3,'Apr':4,'May':5,'Jun':6,
                   'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12})
#print(df)
df_melted = pd.melt(df,id_vars=['Year'])
#print(df_melted)
newcols = {'variable':'Month'}
df_melted.rename(columns=newcols, inplace=True)
df=df_melted.sort_values(by = ['Year','Month'])
#print(df)
df['date_str'] = df['Year'].astype(str) + '-' + df['Month'].astype(str)
df['date'] = pd.to_datetime(df['date_str'], format='%Y-%m')
df.drop('date_str', axis=1, inplace=True)
df = df.loc[(df['value']!=np.nan)]
#print(df)
plt.figure()
plt.plot(df['date'],df['value'],linewidth=2.5)
plt.grid()
plt.xlabel('Date')
plt.ylabel('Rate (%)')
plt.title('Unemployment Rate')
plt.show()
