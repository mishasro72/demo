import requests
from bs4 import BeautifulSoup as bs
import pandas

URL = "https://www.etagi.com/zastr/?studio[]=false&rooms[]=3"
r = requests.get(URL)

print(r.status_code)
