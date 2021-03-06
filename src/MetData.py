'''
Created on Oct 20, 2015

@author: rgargente@gmail.com
'''

from Bio.Statistics.lowess import lowess

import matplotlib.pyplot as plt
import numpy as np


class MetData:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        constructor
        '''
        self.rows = []
        
        
    def add_row(self, year, month, tmax, tmin, rain, sun):
        self.rows.append(MetDataRow(year, month, tmax, tmin, rain, sun))
        
    
    def get_rain_totals(self):
        years = []
        rains = []
        
        prev_year = self.rows[0].year
        count = 0
        rain = 0
        for row in self.rows:
            if (row.year == prev_year):
                count += 1
                rain += row.rain
                if (count == 12):
                    years.append(row.year)
                    rains.append(rain)
            else:
                count = 1
                rain = row.rain
            prev_year = row.year
        return (years, rains)
    
    def plot_rain_by_year(self):
        # Get data
        data = self.get_rain_totals()
        years = np.asarray(data[0]).astype(np.float)
        x_pos = np.arange(len(years))
        rain = np.asarray(data[1])
        
        # Plot bars
        plt.bar(x_pos, rain, align='center', alpha=0.4)
        plt.xticks(x_pos, years)
        plt.tick_params(
            axis='x',
            which='both',
            bottom='off',
            top='off')
        plt.xlabel('Rain')
        
        # Plot average
        avg = np.average(rain)
        plt.axhline(avg)
        
        # Plot trend line
        l = lowess(years, rain, f=0.5)
        plt.plot(l, linestyle='--')
        
        plt.title('Total rain in London per year')
        plt.show()
        
            
class MetDataRow:
    
    def __init__(self, year, month, tmax, tmin, rain, sun):
        self.year = year
        self.month = month
        self.tmax = tmax
        self.tmin = tmin
        self.rain = rain
        self.sun = sun
        
