from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.ptt.cc/bbs/Food/M.1518084265.A.CAE.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml").select('.article-meta-value')
article = BeautifulSoup(res.text, "lxml").select('#main-content')
meta_list=[]
for element in soup:
    meta_list.append(element.text)
for item in article:
    content = item.text
print("日期: "+str(meta_list[3]))
print("標題: "+str(meta_list[2]))
print("看板名稱: "+str(meta_list[1]))
print("作者: "+str(meta_list[0]))
print("內文: "+str(content))