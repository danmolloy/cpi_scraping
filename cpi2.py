import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import time
import requests
from urllib.request import Request, urlopen
import pandas as pd
from pandas.io.json import json_normalize


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = requests.get("https://countryeconomy.com/countries-cpi/ireland")

soup = BeautifulSoup(response.text, "html.parser")

##yy = soup.body.find('div',attrs={'class':'table'})

##x = soup.body.findAll('td',class = 'numero')

x = soup.body.find('td', attrs={'class' : 'numero'}).text
print(x)