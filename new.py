import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('minicalc.ui', self)
        self.setWindowTitle('Миникалькулятор')
        self.show()
        self.pushButton.clicked.connect(self.clickBtn1)

    def clickBtn1(self):
        self.a = int(self.lineEdit.text())
        self.b = int(self.lineEdit_2.text())
        self.lcdNumber.display(str(round(self.a + self.b, 3)))
        self.lcdNumber_2.display(str(round(self.a - self.b, 3)))
        self.lcdNumber_3.display(str(round(self.a * self.b, 3)))
        self.lcdNumber_4.display(str(round(self.a / self.b, 3)) if self.b != 0 else 'error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
