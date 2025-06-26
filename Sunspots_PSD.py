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
#import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

filename = "/home/cgreco/data/Sunspots/SN_m_tot_V2.0.csv"
filename_url = "https://www.sidc.be/SILSO/DATA/SN_m_tot_V2.0.csv"   # Online source
'''
    Read Sunspot Data from local file or online source
    - File format: csv or txt
    - Columns separated by one or more spaces or semicolon
    - Use sep=';' for csv file or sep=r'\s+' for txt file with columns separated by one or more spaces
    - If the file is not found, it will try to read from the online source
    - If both fail, it will print an error message and set df to None
'''
# Attempt to read the local file first
try:
    df = pd.read_csv(filename,sep=';',index_col=False,header=None, \
            names=["Year","Month","Date","Sunspots","Sunspots_SD","Indicator","Provisional"])
except (FileNotFoundError, pd.errors.EmptyDataError):
    try:
        df = pd.read_csv(filename_url,sep=';',index_col=False,header=None, \
            names=["Year","Month","Date","Sunspots","Sunspots_SD","Indicator","Provisional"])
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("Error: Both file1.csv and file2.csv could not be loaded.")
        df = None # Or some default DataFrame
    else:
        print("Sunspot Data from Online source loaded successfully.\n")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Sunspot Data from local folder loaded successfully.\n")

if df is not None:
    # Proceed with operations on the DataFrame
    # Convert Year and Month to Date (YYYY-MM-DD format)
    df["Date"] = pd.to_datetime(df[["Year", "Month"]].assign(Day=1))
    #df["Date"] = pd.to_datetime(df[["Year", "Month"]].assign(Day=1), format='%Y-%m')
    print(df)   # Display DataFrame first and last 5 rows
else:
    print("No data to display. Please check the file paths or URLs.")
    sys.exit(1)

# Design the FIR lowpass filter & filter data
# Order of the filter
# Sampling frequency (cycles/year)
fs = 12     # Once per month (12 times per year)
# Cutoff frequency (cycles/year)
fc = 0.4    # Cutoff frequency cycles/year
order = 12
M1 = order + 1
# Lowpass Filter the Data
# Design the FIR lowpass filter using the window method
h1 = signal.firwin(M1, fc, window='hann', fs = fs)
y_filtered = signal.filtfilt(h1,[1],df["Sunspots"])

# Display Graph of Sunspots
plt.figure(figsize=(12,6))
plt.plot(df["Date"],df["Sunspots"], label='Monthly Averages')
plt.plot(df["Date"], y_filtered, 'r-', linewidth=1.5, label=f'Lowpass Filtered, fc = {fc} Cycles/Year')
plt.xlim(df["Date"].min(), df["Date"].max())
plt.grid()
plt.xlabel("Date (Year)")
plt.ylabel("Sunspot Number $S_n$")
plt.title("Numbers of Sunspots 1749 to Present (Monthly Averages), Lowpass Filtered with Raw Data")
plt.legend()

# Power Spectral Density Estimation
NFFT = 2048
f, Pxx = signal.welch(df["Sunspots"].to_numpy(),fs=fs,window='hann',nperseg=12*90, \
    noverlap=12*40,nfft=NFFT,detrend='linear',return_onesided=True,scaling='density')

plt.figure()
plt.semilogy(f, Pxx)
plt.xlim(0,1)
plt.grid()
plt.xlabel('Frequency (Cycles/Year)')
plt.ylabel('Sunspots**2 - Year')
plt.title('Sunspot Power Spectral Density')
EndRange = int(0.25*NFFT/12)
peaks, _ = signal.find_peaks(Pxx[0:EndRange])
plt.text(0.2,5e4,rf'Peaks: {np.around(peaks*fs/NFFT, decimals=4)} Cycles/Year')
plt.text(0.2,2e4,rf'Periods: {np.around(np.reciprocal(peaks*fs/NFFT), decimals=2)} Years ')
plt.show()
