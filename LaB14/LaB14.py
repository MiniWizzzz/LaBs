# тут импортирую библиотечки
from PyQt5.QtWidgets import *
import sys
from classes.stopwatch import StopWatch

# создание pyqt5 приложения, так гугл насоветовал, я ему верю
App = QApplication(sys.argv)

# создаю само окошко
StopWatch = StopWatch()

# старт приложухи
sys.exit(App.exec())