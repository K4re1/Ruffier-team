# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

def show_second():
    main_win1.hide()
    main_win2.show()

app = QApplication([])
main_win1 = QWidget()
main_win1.setWindowTitle('Тест Руфье: знакомство')
main_win1.move(460, 170)
main_win1.resize(1000, 600)
hello = QLabel('Добро пожаловать в программу по определению состояния вашего здоровья!')
instr_main = QLabel('Проба проводится следующим образом. \n После 5-минутного отдыха у испытуемого измеряют пульс в положении сидя. \n Далее необходимо сделать 30 приседаний за 45 секунд, после чего испытуемый садится и в течение первых 15-ти секунд вновь фиксируются показания пульса. \n Третьим показателем является число сердечных ударов за последние 15 секунд первой минуты отдыха после приседаний.')
button_main = QPushButton('Начать тест')
line_v1 = QVBoxLayout()
line_v1.addWidget(hello, alignment = Qt.AlignLeft)
line_v1.addWidget(instr_main, alignment = Qt.AlignLeft)
line_v1.addWidget(button_main, alignment = Qt.AlignCenter)
main_win1.setLayout(line_v1)
button_main.clicked.connect(show_second)
main_win1.show()
app.exec_()