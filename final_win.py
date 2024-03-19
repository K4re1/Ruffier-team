# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication([])
main_win3 = QWidget()
main_win3.setWindowTitle('Тест Руфье: результаты')
main_win3.move(460, 170)
main_win3.resize(1000, 600)
main_win3.show()
app.exec_()