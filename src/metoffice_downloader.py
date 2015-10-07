'''
Created on Oct 6, 2015

@author: rafa

Downloads data from metoffice.gov.uk
The format of the text file data is:
    yyyy  mm   tmax    tmin      af    rain     sun
    1948   1    8.9     3.3    ---     85.0    ---
'''

import requests

import numpy as np

def download_data():
    url_heathrow = 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt'
    raw = requests.get(url_heathrow).content
    return raw

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def _get_sun(s):
    if is_number(s):
        return s
    s = s[:-1]
    if is_number(s):
        return s 
    else:
        return None

def get_data():
    raw = download_data().splitlines()
    # Filter non data lines (introduction, etc)
    data_lines = [line for line in raw if is_number(line.split()[0])]
    
    data = np.zeros((6, len(data_lines)))
    
    i = 0
    for line in data_lines:
        items = line.split()
        year = items[0]
        month = items[1]
        tmax = items[2]
        tmin = items[3]
        rain = items[5]
        sun = items[6]
        data[0, i] = year
        data[1, i] = month
        data[2, i] = tmax
        data[3, i] = tmin
        data[4, i] = rain if is_number(rain) else None
        data[5, i] = _get_sun(sun)
        i += 1

    return data
