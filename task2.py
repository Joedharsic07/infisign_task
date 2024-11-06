import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://docs.infisign.io/')
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find_all('section', class_='category-list')
data = []

for atag in title:
    anchor = atag.find_all('a', class_='category')
    for anchors in anchor:
        product = "https://docs.infisign.io" + anchors.get('href')
        nextresponse = requests.get(product)
        heading_soup = BeautifulSoup(nextresponse.text, 'html.parser')
        heading = heading_soup.find_all('h1')
        for headings in heading:
            head = headings.get_text()
            link = heading_soup.find_all('ul', class_='articleList')
            for litag in link:  
                links = litag.find_all('a')
                for atag in links:
                    finallink = "https://docs.infisign.io" + atag.get('href')
                    data.append((head, finallink))  

df= pd.DataFrame(data,columns=['head','links'])
df.to_csv('task1.csv',index=False)
