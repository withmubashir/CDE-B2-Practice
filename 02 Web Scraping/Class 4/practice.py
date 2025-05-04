from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
request = requests.get(url)
print(request)

soup = BeautifulSoup(request.content, 'html.parser')
# print(soup)

# price = soup.find('div', class_ ="sc-142c02c-0 lmjbLF rise").text
# name = soup.find('div', class_ = 'sc-4c05d6ef-0 bLqliP').text
# hr1 = soup.find('span', class_ ="sc-1e8091e1-0 jgYsZM").text
# d7 = soup.find('span', class_ ="sc-1e8091e1-0 fDGzbr").text
# marketcap = soup.find('span', class_ ="sc-11478e5d-1 jfwGHx").text
# volume24hr = soup.find('div', class_ ="sc-4c05d6ef-0 sc-cb798334-0 dlQYLv jltLyq").text
# csv = soup.find('div', class_ ="circulating-supply-value").text
# print(name,hr1,d7,marketcap,volume24hr,csv)

tr = soup.find_all('tr')

all_data = []

for trs in tr:
    data = []
    name = soup.find('div', class_ = 'sc-4c05d6ef-0 bLqliP').text
    hr1 = soup.find('span', class_ ="sc-1e8091e1-0 jgYsZM").text
    d7 = soup.find('span', class_ ="sc-1e8091e1-0 fDGzbr").text
    marketcap = soup.find('span', class_ ="sc-11478e5d-1 jfwGHx").text
    volume24hr = soup.find('div', class_ ="sc-4c05d6ef-0 sc-cb798334-0 dlQYLv jltLyq").text
    csv = soup.find('div', class_ ="circulating-supply-value").text
    data = [name,hr1,d7,marketcap,volume24hr,csv]
    all_data.append(data)


print(all_data)
