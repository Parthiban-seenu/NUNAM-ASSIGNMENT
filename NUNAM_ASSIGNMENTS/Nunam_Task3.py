#17MIS0307_PARTHIBAN_S

from scipy.signal import filtfilt
from scipy import stats
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

def plot():
    data = pd.read_csv('.detailVolDownsampled.csv')
    sensor_data = data[['Voltage']]

    sensor_data = np.array(sensor_data)

    time = np.linespace(0, 0.0002, 4000)

    plt.plot(time, sensor_data)
    plt.show()

    filtered_signal = bandPassFilter(sensor_data)

    plt.plot(time, filtered_signal)
    plot.show()

def bandPassFilter(signal):
    fs = 4000.0
    lowcut = 20.0
    highcut = 50.0

    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    order = 2

    b, a = scipy.signal.butter(order, [low, high], 'bandpass', analog=False)
    y = scipy.signal.filtfilt(b, a, signal, axis = 0)

    return(y)