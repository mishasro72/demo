import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
#import fake_useragent

#user = fake_useragent.UserAgent().random
URL_TEMPLATE = "https://www.kinopoisk.ru/lists/movies/top250/"
#URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
#URL_TEMPLATE = "https://tyumen.zarplata.ru/vacancy/kurer?track=rubrics"
r = requests.get(URL_TEMPLATE)
print(r.status_code)
r = r.text
#print(r.text)
soup = bs(r, "html.parser")
vacancia_name = soup.find_all('div', class_= 'styles_root__ti07r styles_watched__GyNVg')
#for name in vacancia_name:
 #   print(name.a)
    #print(name.a['title'])
 #   if name.a in name:
  #      print(name.a['title'])
#vacancia_info = soup.find_all('p', class_='overflow')
#for info in vacancia_info:
 #   print(info.text)
#soup = bs(r.encode('ISO-8859-1'), "html.parser")
print(vacancia_name)
#print(r.text)
