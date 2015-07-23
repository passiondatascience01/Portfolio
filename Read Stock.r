# Read data from Yahoo Finance for N Stocks 
# Go to Yahoo Finance 
# Click on Stocks History Prices
# Choose the Stocks 
# Export into Spreadsheet
# this will save file somewhere on your desktop

# READ APPLE STOCKS
AAPL <- read.csv(file.choose())
str(AAPL)
head(AAPL)


