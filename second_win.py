# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from final_win import *


class Experiment():
   def __init__(self, age, test1, test2, test3):
       self.age = age
       self.t1 = test1
       self.t2 = test2
       self.t3 = test3


class TestWin(QWidget):
   def __init__(self):
       super().__init__()

         self.initUI()

       self.connects()

       self.set_appear()
      
       self.show()

   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


   def initUI(self):

       self.btn_next = QPushButton(txt_sendresults, self)
       self.btn_test1 = QPushButton(txt_starttest1, self)
       self.btn_test2 = QPushButton(txt_starttest2, self)
       self.btn_test3 = QPushButton(txt_starttest3, self)
