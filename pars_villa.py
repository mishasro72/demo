import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://istories.media/investigations/2021/04/07/chudesnaya-villa-na-ostrove-millionerov/"
r = requests.get(URL_TEMPLATE)
#print(r.status_code)
r = r.text
soup = bs(r.encode('ISO-8859-1'), "lxml")
#soup = bs(r, "lxml")
print(soup)
#print(r.text)
