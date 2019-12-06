from bs4 import BeautifulSoup
import requests
with open('html file name') as html_file:
  soup=BeautifulSoup(html_file,'lxml')
print(soup)
