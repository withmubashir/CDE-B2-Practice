from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"
request = requests.get(url)
print(request)

soup = BeautifulSoup(request.content, 'html.parser')
# print(soup)

title = soup.find('h2', class_ = 'title is-5').text
subtitle = soup.find('h3', class_ ="subtitle is-6 company").text
location = soup.find('p', class_ ="location").text
date = soup.find('p', class_ ="is-small has-text-grey").text
print(title,subtitle,location,date)

div = soup.find_all('div', class_ = "column is-half")

all_data = []

for divs in div:
    data = []
    title = soup.find('h2', class_ = 'title is-5').text.strip()
    subtitle = soup.find('h3', class_ ="subtitle is-6 company").text.strip()
    location = soup.find('p', class_ ="location").text.strip()
    date = soup.find('p', class_ ="is-small has-text-grey").text.strip()
    data = [title,subtitle,location,date]
    all_data.append(data)


print(all_data)
