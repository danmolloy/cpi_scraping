import urllib.request
from bs4 import BeautifulSoup
import json
import ssl
import time
import requests
from urllib.request import Request, urlopen
import csv
import os


response = requests.get("https://countryeconomy.com/countries-cpi/ireland")

soup = BeautifulSoup(response.text, "html.parser")


def parse_table(table):
  data = []
  for row in table.select('tbody tr'):
      name = row.select('td')[0].get_text()
      number_cells = row.select('td.numero')
      percentages = list(map(lambda td: td.attrs['data-value'], number_cells))
      data.append({'name': name, 'percentages': percentages})
  return data

table_data = []

for table in soup.select('table'):
  table_data.append(parse_table(table))

if os.path.isfile('cpi.csv'):
  os.remove('cpi.csv')

csvfile = open('cpi.csv', 'w+')
writer = csv.writer(csvfile)
writer.writerow(['Name', 'Interannual', 'YTD', 'Monthly'])

for row in table_data[0]:
  csvrow = row['percentages']
  csvrow.insert(0, row['name'][0:-4])
  writer.writerow(csvrow)
