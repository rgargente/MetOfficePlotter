'''
Created on Oct 6, 2015

@author: rafa
'''

import metoffice_downloader

if __name__ == '__main__':
    data = metoffice_downloader.get_data()
    print(data)