import requests
from bs4 import BeautifulSoup


date = input("Enter a date(yyyy-mm-dd) please enter date after 2022-02-19(we are currently having only data after this date):  ")

URL = f'https://www.billboard.com/charts/india-songs-hotw/{date}'

response = requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')

#select is like css selector
element = soup.select('li ul li h3')
songs = [song.getText().strip() for song in element]
for song in songs:
    print(song)
    