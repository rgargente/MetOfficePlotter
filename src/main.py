'''
Created on Oct 6, 2015

@author: rgargente@gmail.com
'''

import metoffice_downloader
import matplotlib.pyplot as plt

if __name__ == '__main__':
    metdata = metoffice_downloader.get_data()
    metdata.plot_rain_by_year()
    data = metdata.plot_rain_by_year()
    years = data[0]
    rain = data[1]
