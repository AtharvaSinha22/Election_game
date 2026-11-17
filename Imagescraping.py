import requests
from bs4 import BeautifulSoup

url = r"https://www.timesofsports.com/cricket/ipl/all-teams-logo/"
page = requests.get(url)
print(page)
