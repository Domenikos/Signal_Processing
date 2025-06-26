#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Dow Jones Industrial Average (07/03/2023 to 06/28/2024)
    https://www.marketwatch.com/investing/index/djia/download-data?startDate=7/3/2023&endDate=6/28/2024

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

'''
import requests

url = 'https://www.marketwatch.com/investing/index/djia/downloaddatapartial?startdate=06/04/2024%2000:00:00&enddate=07/04/2024%2023:59:59&daterange=d30&frequency=p1d&csvdownload=true&downloadpartial=false&newdates=false'
response = requests.get(url)

df_list = pd.read_html(response.text)
df = df_list[0]
'''

df = pd.read_csv('/home/cgreco/Downloads/DowJones_23_24_new.csv')

# Reverse order from decreasing to increasing chronological order
df = df.iloc[::-1]

# Convert data from string to float type first removing commas
df['Open'] = df['Open'].str.replace(',','').astype(float)
df['High'] = df['High'].str.replace(',','').astype(float)
df['Low'] = df['Low'].str.replace(',','').astype(float)
df['Close'] = df['Close'].str.replace(',','').astype(float)

# Convert date in string format to date data type
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

#print(df)

plt.figure()
#plt.plot(df['Date'],df['Close'])
plt.scatter(df['Date'],df['Close'],label='Data')
plt.grid()
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Dow Jones Industrial Averages')

#plt.show()

# Interpolate data for days market is closed

day_index = pd.date_range(start = df['Date'].min(), end = df['Date'].max(), freq='D')
interp_values = np.interp(day_index, df['Date'], df['Close'])
plt.plot(day_index, interp_values, label='Interpolation')
plt.legend(loc = "best")
#coef = np.polyfit(day_index.to_numpy(), interp_values, 3)
#print(coef)
plt.figure()
detrended_interp_values = signal.detrend(interp_values,type='linear')
plt.plot(day_index,detrended_interp_values)
plt.grid()
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Dow Jones Industrial Averages (Interpolated & Detrended)')


# Power Spectral Density

f, Pxx = signal.welch(detrended_interp_values,fs=1.0,window='hanning',nperseg=60,
        noverlap=30,nfft=256,detrend='linear',return_onesided=True,scaling='density')

plt.figure()
plt.semilogy(f, Pxx)
plt.grid()
plt.xlabel('Frequency (1/day)')
plt.ylabel('Value**2 - Day')
plt.title('Power Spectral Density (Interpolated & Detrended Values)')
plt.show()
