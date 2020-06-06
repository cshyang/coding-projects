import requests
from bs4 import BeautifulSoup
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
print(response.text)
