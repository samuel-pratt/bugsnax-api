## IN PROGRESS
## Does not currently work, will be updating as time goes on

import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Took this off of beautiful soup documentation
def make_soup(url):
  res = requests.get(url, verify=True)
  html_content = res.text
  soup_object = BeautifulSoup(html_content , "html.parser")
  return soup_object

def get_data():
  base_url = 'https://bugsnax.fandom.com'

  grumpuses_link = 'https://bugsnax.fandom.com/wiki/Category:Characters'
  grumpuses_link_class = 'category-page__member-link'

  locations_link = 'https://bugsnax.fandom.com/wiki/Category:Locations'
  locations_link_class = 'category-page__member-link'

  bugsnax_link = 'https://bugsnax.fandom.com/wiki/Bugsnax_(Creatures)'

  # Get links for grumpuses
  url = (grumpuses_link)
  soup = make_soup(url)
  grumpuses_links = []
  for a in soup.find_all("a", {"class": grumpuses_link_class}):
    grumpuses_links.append(base_url + a['href'])

  # Get links for locations
  url = (locations_link)
  soup = make_soup(url)
  locations_links = []
  for a in soup.find_all("a", {"class": locations_link_class}):
    locations_links.append(base_url + a['href'])

  # Get links for bugsnax
  url = (bugsnax_link)
  soup = make_soup(url)
  bugsnax_links = []
  table = soup.find("tbody")
  for a in table.find_all("tr"):
    temp = a.find(title=True)
    if temp:
      bugsnax_links.append(base_url + temp['href'])

  # Get data for grumpuses
  grumpuses_data = []
  for a in grumpuses_links:
    url = (a)
    soup = make_soup(url)
    profile_card = soup.find_all("aside", {"class": 'portable-infobox'})
    for b in profile_card:
      grumpus = {}
      if b.find("h2"):
        grumpus['name'] = b.find("h2").text
      profile_content = b.find_all("section")
    grumpuses_data.append(grumpus)

  return grumpuses_data

# Used for testing
if __name__ == '__main__':
    print(get_data())