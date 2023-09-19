import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://www.kinopoisk.ru'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements by their HTML tags, classes, or IDs
# Here's an example of finding the title of the top movie on the homepage
top_movie_title = soup.find('span', class_='selection-film-item-meta__name').text
print('Top movie title:', top_movie_title)

# You can also find multiple elements and iterate over them
# Here's an example of finding and printing the titles of the top 5 movies on the homepage
top_movies = soup.find_all('span', class_='selection-film-item-meta__name')
print('Top 5 movies:')
for movie in top_movies[:5]:
    print(movie.text)
