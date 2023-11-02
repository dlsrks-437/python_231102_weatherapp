
import sys
import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("UI/weather_app_UI.ui")

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = WeatherWin()
    myApp.show()
    sys.exit(app.exec_())








