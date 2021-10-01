# coding=utf-8

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLineEdit, QMessageBox

from db_handler import db_work
from final_contacts import TableContacts
from forget_password import ForgetPwd
from reg import Registration
from utility import ClickableLineEdit, ClickableLineEdit2, ClickableLineEditFunc


class Main_menu(QWidget):
    def __init__(self, flags=None, *args, **kwargs):
        QWidget.__init__(self, flags, *args, **kwargs)
        self.db = db_work()
        self.setWindowTitle("Окно Авторизации")

        total_layout = QtWidgets.QVBoxLayout()
        fst_layout = QtWidgets.QVBoxLayout()
        snd_layout = QtWidgets.QHBoxLayout()
        third_ladyout = QtWidgets.QVBoxLayout()
        total_layout.addLayout(fst_layout)
        total_layout.addLayout(snd_layout)
        total_layout.addLayout(third_ladyout)
        self.setLayout(total_layout)

        self.pushButton_in = QtWidgets.QPushButton()
        self.pushButton_in.setObjectName("button_auth")

        self.pushButton_in.setStyleSheet("background-color: rgb(230, 230, 0);")
        self.pushButton_in.setText("Войти")
        self.pushButton_in.clicked.connect(self.auth)

        self.pushButton_reg = QtWidgets.QPushButton()
        self.pushButton_reg.setStyleSheet("background-color: rgb(148, 148, 148);")
        self.pushButton_reg.setText("Регистрация")
        self.pushButton_reg.clicked.connect(self.reg)

        self.pushButton_delay = QtWidgets.QPushButton()
        self.pushButton_delay.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_delay.setText("Отмена")

        self.pushButton_delay.clicked.connect(self.delay)

        snd_layout.addWidget(self.pushButton_in)
        snd_layout.addWidget(self.pushButton_reg)
        snd_layout.addWidget(self.pushButton_delay)

        self.lineEdit_login = ClickableLineEdit()
        self.lineEdit_login.setText("Имя пользователя")
        self.lineEdit_password = ClickableLineEdit2()
        self.lineEdit_password.setText("Пароль")

        fst_layout.addWidget(self.lineEdit_login)
        fst_layout.addWidget(self.lineEdit_password)

        self.checkBox_remeber_me = QtWidgets.QCheckBox()
        self.checkBox_remeber_me.setText("Запомнить пароль")

        self.checkBox_show_pass = QtWidgets.QCheckBox()
        self.checkBox_show_pass.setText("Показать пароль")
        self.checkBox_show_pass.toggled.connect(self.show_pwd)
        third_ladyout.addWidget(self.checkBox_remeber_me)
        third_ladyout.addWidget(self.checkBox_show_pass)
        self.label = ClickableLineEditFunc(self.forget_pwd)
        self.label.setText("Забыли пароль?")
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        total_layout.addWidget(self.label, alignment=Qt.AlignHCenter)
        if self.db.check():
            self.setVisible(False)
            self.call_contact()
            self.close()

    def call_contact(self):
        condition = self.db.check()
        contacts = TableContacts(condition[0][0])
        contacts.show()
        self.setVisible(False)
        contacts.exec_()
        self.close()

    def forget_pwd(self):
        forget = ForgetPwd()
        forget.show()
        self.setVisible(False)
        forget.got_signal.connect(self.show_it)
        forget.exec_()

    def show_pwd(self):
        if self.checkBox_show_pass.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def auth(self):
        login = self.lineEdit_login.text().encode('utf8')
        passwd = self.lineEdit_password.text().encode('utf8')
        condition = self.db.auth(login, passwd)
        if condition:
            if self.checkBox_remeber_me.isChecked:
                self.db.fill(condition[0][0])
            contacts = TableContacts(condition[0][0])
            contacts.show()
            self.setVisible(False)
            contacts.got_signal.connect(self.show_it)
            contacts.exec_()
        else:
            QMessageBox.about(self, "аутентификация", "Пользователь с такими данными не найден!")

    def reg(self):
        register = Registration()
        register.show()
        self.setVisible(False)
        register.got_signal.connect(self.show_it)
        register.exec_()

    def show_it(self, the_signal):
        self.setVisible(True)
        if the_signal != "something":
            user_id, login, password = the_signal.split(";")
            contacts = TableContacts(user_id)
            contacts.show()
            self.setVisible(False)
            contacts.exec_()

    def delay(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main_menu()
    window.show()
    sys.exit(app.exec_())
