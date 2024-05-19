# тут импортирую библиотечки
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StopWatch(QMainWindow):

    def __init__(self):
        super().__init__()

        # название окна
        self.setWindowTitle("Секундомер")
        # размер окна --> setGeometry(left, top, width, height)
        self.setGeometry(100, 100, 400, 400)

        # для функции, обрабатывающей параметры компонентов окна
        self.сomponents()

        self.show()

    # функции для компонентов окошка
    def сomponents(self):
        self.label_name = QLabel('Секундомер', self)

        # размер заголовка --> setGeometry(left, top, width, height)
        self.label_name.setGeometry(75, 40, 250, 70)

        # стиль для заголовка
        self.label_name.setFont(QFont('Geometria Medium', 28))

        # выравниваю заголовок по центру, мы ж дизигнеры, а не дурачки какие-нибудь (или да)
        self.label_name.setAlignment(Qt.AlignCenter)

# СЧЕТЧИК

        # счетчик собсна
        self.count = 0

        self.flag = False

        # для указателя времени (поле с счетчиком)
        self.label = QLabel(self)

        # размер для окна с показателями секундомера --> setGeometry(left, top, width, height)
        self.label.setGeometry(75, 120, 250, 70)

        # добавляю цветную обводку и крашу фон, чтобы всё по красоте
        self.label.setStyleSheet("border: 4px solid rgb(205, 237, 252); background-color: rgb(237, 244, 247); border-radius: 10px;", )

        # сюда подкрепляю надпись(счетчик), который прописала ранее
        self.label.setText(str(self.count))

        # стиль для надписи(счетчика) маааксимально стандартный
        self.label.setFont(QFont('Geometria Medium', 24))

        # выравниваю счетчик по центру
        self.label.setAlignment(Qt.AlignCenter)

# КНОПКА СТАРТ

        # кнопка собственной персоной
        start = QPushButton("Поехали!", self)

        # размер кнопухи --> setGeometry(left, top, width, height)
        start.setGeometry(75, 230, 120, 50)

        # добавляю красоту
        start.setStyleSheet("border: none; background-color: rgb(150, 226, 177); border-radius: 6px;", )

        # добавляю стиль
        start.setFont(QFont('Geometria Medium', 12))

        # добавляю действие
        start.pressed.connect(self.Start)

# КНОПКА ПАУЗА

        # сама кнопа
        pause = QPushButton("Пауза", self)

        # размер кнопы --> setGeometry(left, top, width, height)
        pause.setGeometry(205, 230, 120, 50)

        # добавляю красоту
        pause.setStyleSheet("border: none; background-color: rgb(237, 226, 122); border-radius: 6px;", )

        # добавляю стиль
        pause.setFont(QFont('Geometria Medium', 12))

        # добавляю действие
        pause.pressed.connect(self.Pause)

# КНОПКА СБРОС

        # кноп
        re_set = QPushButton("Сбросить", self)

        # разм кноп --> setGeometry(left, top, width, height)
        re_set.setGeometry(75, 290, 250, 50)

        # добавляю красоту
        re_set.setStyleSheet("border: none; background-color: rgb(255, 136, 108); border-radius: 6px;", )

        # добавляю стиль
        re_set.setFont(QFont('Geometria Medium', 12))

        # добавляю действие
        re_set.pressed.connect(self.Re_set)

# мясное мясо, делаю таймер

        # сам таймер
        timer = QTimer(self)

        # действие для таймера
        timer.timeout.connect(self.showTime)

        # обновляю таймер каждую десятую секунду или что-то такое
        timer.start(100)

    # метод для таймера, чтобы показывать текст в окошке для таймера, иначе зачем мы тут собрались
    def showTime(self):
        # проверка флага с увеличеснием счетчика
        if self.flag:
            self.count += 1

        # получаю строку на вывод показателя из count (это всё еще тот самый счетчик)
        text = str(self.count / 10)

        # вывод верхнего text
        self.label.setText(text)

# флажки для кнопух
    def Start(self):
        self.flag = True

    def Pause(self):
        self.flag = False

    def Re_set(self):
        self.flag = False

        # обнуление показателя счетчика, потому что в этом смысл кнопки
        self.count = 0

        # вывод обнуленного счетчика
        self.label.setText(str(self.count))