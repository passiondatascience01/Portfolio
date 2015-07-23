# Read data from Yahoo Finance for N Stocks 
# Go to Yahoo Finance 
# Click on Stocks History Prices
# Choose the Stocks 
# Export into Spreadsheet
# this will save file somewhere on your desktop

# READ APPLE STOCKS
import pandas as pd
AAPL <- pd.read_csv('Documents/R/titanic.csv')
AAPL[1:10]
AAPL.shape
AAPL.describe()
