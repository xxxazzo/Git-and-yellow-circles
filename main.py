from sys import exit, argv
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.drawButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_yellow_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_yellow_circle(self, qp):
        qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        diameter = randint(160, 700)
        qp.drawEllipse(400 - diameter // 2, 400 - diameter // 2, diameter,
                       diameter)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = MyWidget()
    ex.show()
    exit(app.exec_())
