from PyQt5.QtCore import *
from PyQt5.QtWidgets import*

app=QApplication([])

win=QWidget()
win.resize(700,500)
win.setWindowTitle("Python")

enter_login=QLineEdit()

enter_password=QLineEdit()

enter_login.setPlaceholderText("Введи логін")
enter_password.setPlaceholderText("Введи пароль")

login_button=QPushButton("Пароль")

row=QVBoxLayout()

col=QVBoxLayout()

row.addWidget(enter_login)
row.addWidget(enter_password)

col.addLayout(row)

col.addWidget(login_button)
col.setSpacing(2)

win.setLayout(col)


def check_password():
    password=enter_password.text()
    if len(password)<6:
        massage_disabled=QMessageBox()
        massage_disabled.setText("Введи довший пароль ніж 6 символів")
        massage_disabled.show()
        massage_disabled.exec_()
    else:
        massage_disabled=QMessageBox()
        massage_disabled.setText("Пароль підходить")
        massage_disabled.show()
        massage_disabled.exec_()

login_button.clicked.connect(check_password)
win.show()

app.exec_()

