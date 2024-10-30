import requests
from bs4 import BeautifulSoup
import pandas as pd
response = requests.get('https://docs.infisign.io/')
soup=BeautifulSoup(response.text,'html.parser')
title=soup.find_all('section', class_='category-list')
data=[]
for atag in title:
    anchor=atag.find_all('a',class_='category')
    for anchors in anchor:
        product="https://docs.infisign.io"+anchors.get('href')
        nextresponse=requests.get(product)
        heading_soup=BeautifulSoup(nextresponse.text,'html.parser')
        heading=heading_soup.find_all('h1')
        for h in heading:
            head=h.get_text()
        links=[]
        link=heading_soup.find_all('ul',class_='articleList')
        for ul in link:
            litag=ul.find_all('li')
            for  li in litag:
                atag=li.find('a')
                links.append("https://docs.infisign.io"+atag.get('href'))
        data.append((head,links))
df= pd.DataFrame(data,columns=['head','links'])
df.to_csv('task.csv',index=False)