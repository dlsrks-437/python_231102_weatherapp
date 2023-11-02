# beautifulsoup4
# requests


import requests

from bs4 import BeautifulSoup

# area = '한남동'

area = input('날씨를 알려드립니다 : ')

weather_html = requests.get(f'https://search.naver.com/search.naver?query={area} 날씨')
# print(weather_html.text)

weather_soup = BeautifulSoup(weather_html.text, 'html.parser')


today_temp = weather_soup.find('div', {'class' : 'temperature_text'}).text
today_temp = today_temp[6:].strip()
print(today_temp)  # 현재 온도


area_text = weather_soup.find('h2', {'class' : 'title'}).text
print(area_text)  # 장소 지명


weather_text = weather_soup.find('span', {'class' : 'weather before_slash'}).text
print(weather_text)  # 날씨


yester_wether = weather_soup.find('p', {'class' : "summary"}).text
yester_wether = yester_wether[:13].strip()
print(yester_wether)  # 어제 대비 온도변화


temp_feel1 = weather_soup.find('div',{'class':'weather_info'}).find('dl',{'class':'summary_list'}).find('dd',{'class':'desc'}).text
print(temp_feel1)

temp_feel2 = weather_soup.find('div', {'class' : "sort"}).text
temp_feel2 = temp_feel2.strip()
print(temp_feel2)  # 체감온도


dust_info = weather_soup.select('ul.today_chart_list>li')
# print(dust_info)
dust1_info = dust_info[0].find('span', {'class' : "txt"}).text
print(dust1_info)  # 미세먼지
dust2_info = dust_info[1].find('span', {'class' : "txt"}).text
print(dust1_info)  # 초미세먼지

part_matter = weather_soup.find('span', {'class' : "txt"}).text
print(part_matter)  # 미세먼지






