import requests
from bs4 import BeautifulSoup
import pandas as pd
data = []

response = requests.get('https://docs.infisign.io/')
soup = BeautifulSoup(response.text, 'html.parser')
mainlink = soup.find_all('a', class_='category')
for anchortag in mainlink:
    product = "https://docs.infisign.io" + anchortag.get('href')
    nextresponse = requests.get(product)
    heading_soup = BeautifulSoup(nextresponse.text, 'html.parser')
    headings = heading_soup.find('h1')
    finalhead = headings.get_text()  
    article_list = heading_soup.find_all('ul', class_='articleList')
    for listtag in article_list:  
        links = listtag.find_all('a')
        for link in links:
            finallink = "https://docs.infisign.io" + link.get('href')
            if finallink not in data:
                data.append((finalhead, finallink))  
print((data))
df= pd.DataFrame(data,columns=['category','links'])
df.to_csv('task1.csv',index=False)
