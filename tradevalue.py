from PyQt5.QtCore import *
from PyQt5.QtWidgets import*

app=QApplication([])

win=QWidget()
win.resize(700,500)
win.setWindowTitle("Python")


value_usdt=QLineEdit()

value_usdt.setPlaceholderText("Долари")


trade=QPushButton("Обмін")

row=QVBoxLayout()

col=QVBoxLayout()

row.addWidget(value_usdt)


col.addLayout(row)

col.addWidget(trade)
col.setSpacing(2)

win.setLayout(col)

def check_trade():
    usdt=value_usdt.text()
    usdt=int(usdt)*42
    grn=QMessageBox()
    grn.setText("Твої гривні"+str(usdt))
    
    grn.show()
    grn.exec_()

trade.clicked.connect(check_trade)


win.show()

app.exec_()
