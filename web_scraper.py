#Web Scraper
import requests
from bs4 import BeautifulSoup

#Download the web page
url = "http://quotes.toscrape.com"
response = requests.get(url)

#Turn the raw web page content into readable structure
soup = BeautifulSoup(response.text, "html.parser")

