# beautifulsoup4
# requests


import requests

from bs4 import BeautifulSoup

area = '한남동'

weather_html = requests.get(f'https://search.naver.com/search.naver?query={area} 날씨')
print(weather_html.text)

weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

today_temp = weather_soup.find('div', {'class' : 'temperature_text'}).text
today_temp = today_temp[6:11]
print(today_temp)


