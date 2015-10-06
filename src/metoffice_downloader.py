'''
Created on Oct 6, 2015

@author: rafa
'''

import requests

url_heathrow = 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt'

def get_data():
    raw = requests.get(url_heathrow).content
    return raw
