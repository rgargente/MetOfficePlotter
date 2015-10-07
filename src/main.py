'''
Created on Oct 6, 2015

@author: rafa
'''

import metoffice_downloader
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = metoffice_downloader.get_data()
    
    years = data[0]
    tmax = data[2]
    
    plt.plot(years, tmax)
    plt.show()