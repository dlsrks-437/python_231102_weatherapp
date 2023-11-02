# beautifulsoup4
# requests


import requests

from bs4 import BeautifulSoup


weather_html = requests.get('https://search.naver.com/search.naver?query=날씨')
print(weather_html.text)


