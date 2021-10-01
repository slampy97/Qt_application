# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QDialog, QLineEdit, QMessageBox

from final_contacts import TableContacts
from utility import ClickableLineEdit
import mysql.connector as mariadb
from dateutil.parser import parse


class Registration(QtWidgets.QDialog):
    got_signal = pyqtSignal(str)

    def On_buttonclick_clicked(self):
        self.setVisible(False)
        self.got_signal.emit("something")

    def __init__(self, flags=None, *args, **kwargs):
        QDialog.__init__(self, flags, *args, **kwargs)
        self.setWindowTitle("Регистрация")
        total_layout = QtWidgets.QVBoxLayout()
        fst_layout = QtWidgets.QHBoxLayout()
        snd_layout = QtWidgets.QHBoxLayout()
        third_layout = QtWidgets.QHBoxLayout()
        four_layout = QtWidgets.QHBoxLayout()
        fifth_layout = QtWidgets.QHBoxLayout()
        total_layout.addLayout(fst_layout)
        total_layout.addLayout(snd_layout)
        total_layout.addLayout(third_layout)
        total_layout.addLayout(four_layout)
        total_layout.addLayout(fifth_layout)
        self.setLayout(total_layout)

        self.login_line = ClickableLineEdit()
        self.login_line.setText("Имя пользователя")
        fst_layout.addWidget(self.login_line)
        self.pwd_line = ClickableLineEdit()
        self.pwd_line.setText("Пароль")
        snd_layout.addWidget(self.pwd_line)

        self.pwd_line_again = ClickableLineEdit()
        self.pwd_line_again.setText("Повторите пароль")
        third_layout.addWidget(self.pwd_line_again)

        self.bith_day_line = ClickableLineEdit()
        self.bith_day_line.setText("День рождения")
        four_layout.addWidget(self.bith_day_line)

        self.ok_button = QtWidgets.QPushButton()
        self.ok_button.setText("Ок")
        self.ok_button.setStyleSheet("background-color: rgb(230, 230, 0);")
        self.ok_button.clicked.connect(self.check)

        self.decline_button = QtWidgets.QPushButton()
        self.decline_button.setText("Отмена")
        self.decline_button.setStyleSheet("background-color: rgb(250, 0, 0)")
        self.decline_button.clicked.connect(self.On_buttonclick_clicked)

        fifth_layout.addWidget(self.ok_button)
        fifth_layout.addWidget(self.decline_button)

    def check(self):
        name = self.login_line.text().encode('utf-8')
        pwd = self.pwd_line.text().encode('utf-8')
        pwd2 = self.pwd_line_again.text().encode('utf-8')
        birth = self.bith_day_line.text().encode('utf-8')
        try:
            parse(birth, fuzzy=False)
        except ValueError:
            QMessageBox.about(self, "Регистрация", "Пишите дату в формате ****-**-**")
            return
        if pwd != pwd2:
            QMessageBox.about(self, "Регистрация", "Пароли не совпадают!")
            return
        year = parse(birth).year
        month = parse(birth).month
        day = parse(birth).day
        final_date_str = "{}-{}-{}".format(year, month, day)
        conn = mariadb.connect(user='root', password='root', host='localhost', port='3306', autocommit=True)
        cursor = conn.cursor()
        cursor.execute("use test;")
        cursor.execute("select * from users where login=\"{}\" and password=\"{}\";".format(name, pwd))
        if cursor.fetchall():
            QMessageBox.about(self, "Регистрация", "Такой пользователь уже есть")
            return
        cursor.execute(
            "insert into users(login, password, birthday) values (\"{}\",\"{}\", \"{}\")".format(
                name, pwd, final_date_str))

        cursor.execute("select * from users where login=\"{}\" and password=\"{}\";".format(name, pwd))
        record = cursor.fetchall()
        user_id, login, password , datetime_obj = record[0][0], record[0][1], record[0][2], record[0][3]
        self.got_signal.emit("{};{};{}".format(user_id, login.encode('utf-8'), password.encode('utf-8'), final_date_str.encode('utf-8')))
        cursor.close()
        conn.close()
        self.close()

