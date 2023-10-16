# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:51:15 2023

@author: lucas
"""

import urllib.request
import gzip
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


####Download a tick-by-tick data from Kraken Exchange through the 
####bitcoincharts.com API

# Data Source
bitcoin_file = "krakenEUR.csv.gz"
URL = "http://api.bitcoincharts.com/v1/csv"
source_file = f"{URL}/{bitcoin_file}"

# Data destination on local disk
dataDir = "C:/Users/lucas/Desktop/github project"
dest_file = f"{dataDir}/{bitcoin_file}"

# Download to disk
urllib.request.urlretrieve(source_file, dest_file)

# Uncompress .gz file and read into a data frame
with gzip.open(dest_file, 'rb') as f_in:
    with open(dest_file[:-3], 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

Bitcoin = pd.read_csv(dest_file[:-3], header=None)


print(Bitcoin[:5])

Bitcoin.columns = ["unixtime", "price", "amount"]

# Display the first 5 rows
print(Bitcoin[:5])

# Extract Variables
Bitcoin['time'] = pd.to_datetime(Bitcoin['unixtime'], unit='s')

# Rearrange columns for ease of reading
Bitcoin = Bitcoin[['time', 'price', 'amount']]

print(Bitcoin[:5])


# Convert the 'Timestamp' column to datetime
Bitcoin['time'] = pd.to_datetime(Bitcoin['time'])


# Set 'Timestamp' as the index
Bitcoin.set_index('time', inplace=True)
