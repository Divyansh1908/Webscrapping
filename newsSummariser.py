# Program to get the first 20 headline and article links from the home page of CNN News US
import requests
from bs4 import BeautifulSoup

# website URL
url = "https://www.cnn.com/us"

# scrape the website for article data
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# articles = soup.find_all('article')
articles = soup.find_all('div', {'class': 'container__headline container_lead-plus-headlines__headline'})
linkus = soup.find_all('a', {'class': 'container__link container_lead-plus-headlines__link'})
title = []
links = []
# extract the title, link, and summary of each article
for article in articles:
    title.append(article.get_text())

for works in linkus:
    links.append(works['href'])

for i in range(20):
    print(title[i],links[i])
