'''
    Sunspot Number - Power Spectral Density
    Download Sunspot Data and Estimate Power Spectral Density
    Solar Influences Data Analysis Center (WDC-SILSO) [https://www.sidc.be/SILSO/home]
    Royal Observatory of Belgium, Brussels
    % Input data Monthly mean total sunspot number (1/1749 - 8/2024)
    Columns separated by one or more spaces
        Column 1-2: Gregorian calendar date
            - Year
            - Month
        Column 3: Date in fraction of year.
        Column 4: Monthly mean total sunspot number.
        Column 5: Monthly mean standard deviation of the input sunspot numbers.
        Column 6: Number of observations used to compute the monthly mean total
                sunspot number.
        Column 7: Definitive/provisional marker. A blank indicates that the value is
                definitive. A '*' indicates that the value is still provisional.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# filename should include the full address of the data on your computer
filename = "/home/cgreco/Downloads/SN_m_tot_V2.0.txt"

df = pd.read_csv(filename,sep='\s+',index_col=False,header=None,
    names=["Year","Month","Date","Sunspots","Sunspots_SD","Indicator","Provisional"])

# Design the FIR lowpass filter & filter data
# Order of the filter
# Sampling frequency (cycles/year)
fs = 12
# Cutoff frequency (cycles/year)
fc = 0.4
order = 12
M1 = order + 1
# Design a Lowpass Filter and apply to the data using the filtfilt function

# Display Graph of Sunspots
plt.figure(figsize=(12,6))
plt.plot(df["Date"],df["Sunspots"], label='Monthly Averages')
# Add code to plot the filtered data on the same graph as the unfiltered data

plt.grid()
plt.xlabel("Date (Year)")
plt.ylabel("Sunspot Number $S_n$")
plt.title("Numbers of Sunspots (Monthly Averages)")
plt.legend()

plt.show()
