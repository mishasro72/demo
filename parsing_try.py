import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
#import fake_useragent

#user = fake_useragent.UserAgent().random
#URL_TEMPLATE = "https://www.kinopoisk.ru/lists/movies/top250/"
pars_list = {'href': [], 'title': [], 'about' : []}
FILE_NAME = "test.csv"
for i in range(1, 3):
    URL_TEMPLATE = f"https://www.work.ua/ru/jobs-odesa/?page={i}"
#URL_TEMPLATE = "https://tyumen.zarplata.ru/vacancy/kurer?track=rubrics"
    r = requests.get(URL_TEMPLATE)
  #  print(r.status_code)
    r = r.text
#print(r.text)
    soup = bs(r, "html.parser")
#vacancia_name = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link js-hot-block')
    vacancia_name = soup.find_all('h2', class_= "")
#vacancia_name = vacancia_name.find('h2', class_= '')
    #for name in vacancia_name:
        #print(name.a['title'])
     #   if name.a in name:
      #      print(name.a['title'])
    #print(len(vacancia_name))
    vacancia_info = soup.find_all('p', class_='overflow')
    for name in vacancia_name:
        if name.a in name:
            pars_list['title'].append(name.a['title'])
            pars_list['href'].append('https://www.work.ua' + name.a['href'])
        
print(pars_list)
#for i in pars_list['title'].values():
 #   print(i)
df = pd.DataFrame(pars_list['title'], pars_list['href'])
#print(df)
df.to_csv(FILE_NAME)
#soup = bs(r.encode('ISO-8859-1'), "html.parser")
#print(soup)
#print(r.text)
