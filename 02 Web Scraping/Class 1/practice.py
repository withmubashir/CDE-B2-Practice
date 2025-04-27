import requests
from bs4 import BeautifulSoup
url = 'https://www.rozee.pk/job/jsearch/q/Python%20Developer'
response = requests.get(url)
