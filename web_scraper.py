#Web Scraper
import requests
from bs4 import BeautifulSoup

#Download the web page
url = "http://quotes.toscrape.com"
response = requests.get(url)

#Turn the raw web page content into readable structure
soup = BeautifulSoup(response.text, "html.parser")

#Find all quote blocks on the page
quote_blocks = soup.find_all("div", class_="quote")

#Loop through each block and extract the details
for block in quote_blocks:
    #Get the text inside 