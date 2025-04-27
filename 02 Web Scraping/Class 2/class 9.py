import requests #to use http protocols
from bs4 import BeautifulSoup
import json
import re
#step # 01
#identifying the url or website 
url = 'https://www.thriftbooks.com/browse/?b.search=%2Cm%2C#b.s=mostPopular-desc&b.p=1&b.pp=50&b.oos&b.tile'

# step#2a
# parsing the content of the url

content = requests.get(url).content
soup = BeautifulSoup(content, 'html.parser')

# print(content)

# step2b
# Transforming and Filtering the data

data = soup.find_all('script')
string = data[12].string
match = re.search(r'window\.searchStoreV2\s*=\s*(\{.*?\});', string, re.DOTALL)
if match:
    works = match.group(1)
    works_json =json.loads(works)
    works = works_json.get('works')
    with open('thrift_books_data.csv', 'a') as f:   
        f.write(f'title , conditio ,buy_pric\n'   )


for i in works:
    data.update(i)
    title = data.title
    condition = data['boyNowCondition']
    buy_price = data['buyNowPrice']

    with open('thrift_books_data.csv', 'a') as f:   
        f.write(f'{title} ,  {condition} , {buy_price}\n'   )

print(data)

json.load(dict(con[12].get_text()))