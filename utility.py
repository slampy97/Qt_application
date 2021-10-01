from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit


class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        self.setText("")
        QLineEdit.mousePressEvent(self, event)


class ClickableLineEditFunc(QLineEdit):
    clicked = pyqtSignal()

    def __init__(self, func, *__args):
        QLineEdit.__init__(self, *__args)
        self.func = func

    def mousePressEvent(self, event):
        self.clicked.emit()
        self.func()
        QLineEdit.mousePressEvent(self, event)


class ClickableLineEdit2(QLineEdit):
    clicked = pyqtSignal()
    i = 1

    def mousePressEvent(self, event):
        self.clicked.emit()
        if ClickableLineEdit2.i == 1:
            self.setEchoMode(QLineEdit.Password)
            ClickableLineEdit2.i += 1
        self.setText("")
        QLineEdit.mousePressEvent(self, event)
