import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import ast
import dateutil.parser as dparser
from datetime import datetime
import re



f = open('C:/Users/Vinh/Desktop/pandas and matplotlib/res.txt','r', encoding='utf-8')

df = pd.read_json(f,orient='records', encoding='utf-8')
matches = []
for dateString in df['pub_date']:
    date = dparser.parse(dateString,fuzzy=True)
    matches.append(date.year)

df['pub_date'] = matches
links = []
for link in df['link']:
    m = re.search('https://dantri.com.vn/(.+?)/', link).group(1)
    links.append(m)
df['link'] = links
df = pd.DataFrame.drop(df,columns=['title','description','tags'])
df = df[df.author.notnull()]

plt.figure(figsize=(6.6,10))
plt.suptitle('Số lượng bài theo chủ đề',fontsize = 16)
n_link = df['link'].value_counts()
n_link = n_link[n_link.values > 50]
plt.barh(n_link.index,width=n_link.values, height=0.8)
plt.xlabel('Số lượng bài')
plt.ylabel('Chủ đề')

plt.figure(figsize=(7,7))
plt
n_author = df['author'].value_counts()
n_author = n_author[n_author.values > 70]
plt.barh(n_author.index,width=n_author.values, height=0.8)
plt.suptitle('Số bài theo tác giả',fontsize = 16)
plt.xlabel('Số lượng bài')
plt.ylabel('Tác giả')

plt.figure(figsize=(5,5))
n_year = df['pub_date'].value_counts()
n_year = n_year[n_year.values>200]
plt.pie(n_year.values,labels = n_year.index,autopct='%1.2f%%', labeldistance = 1.2 )
plt.suptitle('Số bài theo năm',fontsize = 16)

plt.show()

