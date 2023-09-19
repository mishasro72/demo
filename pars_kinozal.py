import requests
from bs4 import BeautifulSoup as bs
import pandas

top_kinozal = []
URL = "https://kinozal.tv/top.php"
r = requests.get(URL)
soup = bs(r.text, "html.parser")
films = soup.find('div', class_="bx1 stable")
films_1 = films.find_all('a', class_='')
for film in films_1:
    top_kinozal.append(film.get('title'))
print(len(films_1))
df = pandas.DataFrame(top_kinozal)
df.to_csv('/Users/milenka/Desktop/kinozal.cvs', sep = " ", encoding='utf8')
print(df)
#for i in top_kinozal:
 #   print(i)

