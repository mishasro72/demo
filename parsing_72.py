import requests
from bs4 import BeautifulSoup as bs
import pandas

news_72 = []
URL = "https://72.ru/"
r = requests.get(URL)
soup = bs(r.text, "html.parser")
news = soup.find_all('div', class_= "_1kPXO")
#print(len(news))
for new in news:
    news_72.append(new.a['title'])
#print(news_72)    
df = pandas.DataFrame(news_72)
df.to_csv('/Users/milenka/Desktop/news_72(05.05).cvs', sep = " ", encoding='utf8')
print(df)
