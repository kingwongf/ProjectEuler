import requests
from bs4 import BeautifulSoup
from decimal import Decimal
#from datetime import *
from dateutil.tz import gettz
import datetime as datetime
import pytz
import re

class ScrapePrices(object):

	def __init__(self, html_file_path=None):
		self.html_file_path = html_file_path

	def get_data_from_url(self, url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}):
		return requests.get(url, headers=headers)

	def get_soup_data(self, url):
		return BeautifulSoup(self.get_data_from_url(url).text, 'html.parser')


	def get_yahoo_price(self,soup):
		timeOfPrice =soup.find('span',attrs={'data-reactid':'38'}).text
		return soup.find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text, 'YAHOO', self.convert_to_utc(timeOfPrice)

	def get_bloomberg_price(self, soup):
		return

	def detect_source_and_parse_data(self, url):
		soup = self.get_soup_data(url)
		if 'yahoo' in url:
			return self.get_yahoo_price(soup)
		if 'bloomberg' in url:
			return self.get_bloomberg_price(soup)


#url_YAHOO = 'https://uk.finance.yahoo.com/quote/GBPUSD%3DX?p=GBPUSD%3DX'
url_BLOOM = 'https://www.bloomberg.com/quote/GBPUSD:CUR'

k = ScrapePrices()

soup =k.get_soup_data(url_BLOOM)
print(soup)
#print(soup.find('span',attrs={'id':'quote_val'}).get_text())
print(soup.find('script',attrs={'class':'priceText__1853e8a5'}))