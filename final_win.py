# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)