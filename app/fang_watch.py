import pandas as pd
import pandas_datareader
import numpy as np
from pandas_datareader import data
from collections import OrderedDict
import datetime
from datetime import date, timedelta
import getpass
import csv

user_name = getpass.getuser()

print("----------------------------")
print("FANG STOCKS: DAILY UPDATE")
print("----------------------------")
print("Welcome, " + (user_name) + "!")
print("")

# INFO TO BE REQUESTED

products = []

new_FANG = ['FB', 'AAPL', 'NVDA', 'GOOG']
stocks_source = 'google'
start = datetime.datetime(2017,1,1) # start = (datetime.date.today() - timedelta(days=5))
end = datetime.date.today()

request = data.DataReader(new_FANG, stocks_source, start, end)

dop = request.ix["Open"] ## dop = daily closing price

dop = dop.to_dict('index')

dop = OrderedDict(sorted(dop.items(), reverse=True)) # h/t https://stackoverflow.com/a/15743140/670433

# facebook = data.DataReader("FB", "google", start, end) # original request per ticker
# apple = data.DataReader("AAPL", "google", start, end)
# nvidia = data.DataReader("NVDA", "google", start, end)
# google = data.DataReader("GOOG", "google", start, end)

menu = """
----------------------------------------
FANG Activity:
----------------------------------------

Date       | FB           | AAPL         | NVDA         | GOOG
---------- | ------------ | ------------ | ------------ | ------------"""

print(menu)

for beginning_of_day in dop:
    symbol_prices = dop[beginning_of_day]
    date = str(beginning_of_day.date())
    fb_usd = '${0:.2f}'.format(symbol_prices["FB"])
    aapl_usd = '${0:.2f}'.format(symbol_prices["AAPL"])
    nvda_usd = '${0:.2f}'.format(symbol_prices["NVDA"])
    goog_usd = '${0:.2f}'.format(symbol_prices["GOOG"])
    print(date, "|", fb_usd, "     |", aapl_usd, "     |", nvda_usd, "     |", goog_usd)

#
# WRITE TO csv
#

#
# t = datetime.datetime(2017,1,1)
# t.strftime('%m/%d/%Y')

csv_file_path = r"C:\Users\Jason\Desktop\Freestyle_project\data\fangs_out.csv"

headers = ["DATE", "FB", "AAPL", "NVDA", "GOOG"]

def csv_writer(beginning_of_day, csv_file_path):
    with open(csv_file_path, "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=headers)
        writer.writeheader()

np.savetxt(csv_file_path, (date, fb_usd, aapl_usd, nvda_usd, goog_usd), delimiter=';') ## using numpy

# df.to_csv(csv_file_path) ## using pandas DataFrame
