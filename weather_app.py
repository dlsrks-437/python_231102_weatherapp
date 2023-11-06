
import sys
import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("UI/weather_app_UI.ui")[0]

class WeatherWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("오늘의 날씨")
        self.setWindowIcon(QIcon('icon/weather_app.png'))
        self.statusBar().showMessage("Weather Application Ver 1.0")

        self.temp_find.clicked.connect(self.request_weather)


    def request_weather(self):
        area = self.location.text()
        weather_html = requests.get(f'https://search.naver.com/search.naver?query={area} 날씨')
        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

        area_text = weather_soup.find('h2', {'class': 'title'}).text
        self.temp_loc.setText(area_text)

        today_temp = weather_soup.find('div', {'class': 'temperature_text'}).text
        today_temp = today_temp[6:].strip()
        self.temperature.setText(today_temp)

        weather_text = weather_soup.find('span', {'class': 'weather before_slash'}).text
        self.weather.setText(weather_text)

        yester_wether = weather_soup.find('p', {'class': "summary"}).text
        yester_wether = yester_wether[:13].strip()
        self.temp_yesterday.setText( yester_wether )

        temp_feel1 = weather_soup.find('div', {'class': 'weather_info'}).find('dl', {'class': 'summary_list'}).find(
            'dd', {'class': 'desc'}).text
        self.temp_feel.setText(temp_feel1)

        dust_info = weather_soup.select('ul.today_chart_list>li')
        dust1_info = dust_info[0].find('span', {'class': "txt"}).text  # 미세먼지
        self.par_matt.setText(dust1_info)
        dust2_info = dust_info[1].find('span', {'class': "txt"}).text  # 초미세먼지
        self.par_matt.setText(dust2_info)


    def WeatherImage(self, weather_text):
        # 날씨 종류 : 맑음, 흐림, 눈, 비, 구름 많음 등...
        if weather_text == '눈' :
            weather_img = QPixmap("icon/snow.png")
        elif weather_text == '비' :
            weather_img = QPixmap("icon/rain.png")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = WeatherWin()
    myApp.show()
    sys.exit(app.exec_())








