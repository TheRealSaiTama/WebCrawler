# To make a web crawler that finds all links and need to create two list
# list crawled will be put in crawled list and one will be not crawled list
# python
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Archive'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
