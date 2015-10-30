'''
Created on Oct 6, 2015

@author: rgargente@gmail.com

Downloads data from metoffice.gov.uk
The format of the text file data is:
    yyyy  mm   tmax    tmin      af    rain     sun
    1948   1    8.9     3.3    ---     85.0    ---
'''

import requests

import numpy as np
from MetData import MetData

def download_data():
    url_heathrow = 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt'
    raw = requests.get(url_heathrow).content
    return raw

def is_number(s):
    if (s is None):
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def _remove_trailing_non_number(s):
    if s is None:
        return None
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
    
    data = MetData()
    for line in data_lines:
        items = line.split()
        year = int(items[0])
        month = int(items[1])
        tmax = float(_remove_trailing_non_number(items[2]))
        tmin = float(_remove_trailing_non_number(items[3]))
        rain = _remove_trailing_non_number(items[5])
        rain = float(rain) if is_number(rain) else None
        sun = _remove_trailing_non_number(items[6])
        sun = float(sun) if is_number(sun) else None
        data.add_row(year, month, tmax, tmin, rain, sun)

    return data
