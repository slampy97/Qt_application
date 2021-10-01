# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QDialog, QLineEdit, QSizePolicy

from utility import ClickableLineEdit


class ForgetPwd(QtWidgets.QDialog):
    got_signal = pyqtSignal(str)

    def On_buttonclick_clicked(self):
        self.setVisible(False)
        self.got_signal.emit("something")

    def __init__(self, flags=None, *args, **kwargs):
        QDialog.__init__(self, flags, *args, **kwargs)
        self.setWindowTitle("Восстановления пароля")
        self.resize(250, 200)
        total_layout = QtWidgets.QVBoxLayout()
        self.line = ClickableLineEdit()
        self.line.setText("Адрес электронной почты")
        total_layout.addWidget(self.line)
        fst_layout = QtWidgets.QHBoxLayout()
        self.btn1 = QtWidgets.QPushButton()
        self.btn1.setText("Сменить пароль")
        self.btn1.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.btn2 = QtWidgets.QPushButton()
        self.btn2.setText("Отмена")
        self.btn2.setStyleSheet("background-color: rgb(240, 0, 0);")
        self.btn2.clicked.connect(self.On_buttonclick_clicked)
        fst_layout.addWidget(self.btn1)
        fst_layout.addWidget(self.btn2)
        total_layout.addLayout(fst_layout)
        self.setLayout(total_layout)
