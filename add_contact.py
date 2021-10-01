# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import mysql.connector as mariadb
import sys

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QDialog, QLineEdit, QTableWidgetItem, QStyle, QMessageBox

from db_handler import db_work
from utility import ClickableLineEdit
from dateutil.parser import parse

class WorkWithContact(QtWidgets.QDialog):
    got_signal = pyqtSignal(str)

    def __init__(self, user, mode, flags=None, *args, **kwargs):
        QDialog.__init__(self, flags, *args, **kwargs)
        self.mode = mode
        self.cur_user=user
        self.resize(300, 100)
        layout = QtWidgets.QVBoxLayout()
        if self.mode == 0:
            self.setWindowTitle("Новый контакт")
        elif self.mode == 1:
            self.setWindowTitle("Удаление контакта")
        else:
            self.setWindowTitle("Модифицирование контакта")
        self.setLayout(layout)
        self.line1 = ClickableLineEdit()
        self.line1.setText("Имя")
        self.line2 = ClickableLineEdit()
        self.line2.setText("Телефон")
        self.line3 = ClickableLineEdit()
        self.line3.setText("Дата рождения")
        layout.addWidget(self.line1)
        layout.addWidget(self.line2)
        layout.addWidget(self.line3)
        if self.mode == 2:
            update_layout = QtWidgets.QVBoxLayout()
            layout.addLayout(update_layout)
            self.line4 = ClickableLineEdit()
            self.line4.setText("[модифиц.] имя")
            self.line5 = ClickableLineEdit()
            self.line5.setText("[модифиц.] телефон")
            self.line6 = ClickableLineEdit()
            self.line6.setText("[модифиц.] день рождения")
            update_layout.addWidget(self.line4)
            update_layout.addWidget(self.line5)
            update_layout.addWidget(self.line6)
        snd_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(snd_layout)
        self.btn1 = QtWidgets.QPushButton()
        if self.mode == 0:
            self.btn1.setText("записать")
        elif self.mode == 1:
            self.btn1.setText("удалить")
        else:
            self.btn1.setText("заменить")
        snd_layout.addWidget(self.btn1)
        self.btn1.clicked.connect(self.check)

    def check(self):
        name, phone, birthday = self.line1.text().encode('utf-8'), self.line2.text().encode('utf-8'), self.line3.text().encode('utf-8')
        try:
            parse(birthday, fuzzy=False)
        except ValueError:
            QMessageBox.about(self, "Регистрация", "Пишите дату в формате ****-**-**")
            return
        year = parse(birthday).year
        month = parse(birthday).month
        day = parse(birthday).day
        final_birth_day = "{}-{}-{}".format(year, month, day)
        conn = mariadb.connect(user='root', password='root', host='localhost', port='3306')
        cursor = conn.cursor()
        cursor.execute("use test;")
        cursor.execute(
            "select * from contacts where name=\"{}\" and phone_number=\"{}\" and birthday=\"{}\" and user_id=\"{}\";".format(
                name, phone, final_birth_day, self.cur_user))

        if self.mode == 0:
            if cursor.fetchall():
                QMessageBox.about(self, "Поменяйте данные контакта", "Такой контакт уже существует")
            else:
                self.got_signal.emit("{};{};{}".format(name, phone, final_birth_day))
                self.close()
        elif self.mode == 1:
            if not cursor.fetchall():
                QMessageBox.about(self, "Поменяйте данные контакта", "Такого контакт нет")
            else:
                self.got_signal.emit("{};{};{}".format(name, phone, final_birth_day))
                self.close()
        else:
            query_res = cursor.fetchall()
            check1 = query_res != []
            if not check1:
                QMessageBox.about(self, "Неверные данные", "такого контакт не существует")
                return
            name2, phone2, birthday2 = self.line4.text().encode('utf-8'), self.line5.text().encode(
                'utf-8'), self.line6.text().encode('utf-8')

            try:
                parse(birthday2, fuzzy=False)
            except ValueError:
                QMessageBox.about(self, "Регистрация", "Пишите дату в формате ****-**-**")
                return
            year2 = parse(birthday2).year
            month2 = parse(birthday2).month
            day2 = parse(birthday2).day
            final_birth_day2 = "{}-{}-{}".format(year2, month2, day2)
            cursor.execute(
            "select * from contacts where name=\"{}\" and phone_number=\"{}\" and birthday=\"{}\" and user_id=\"{}\";".format(
                name2, phone2, final_birth_day2, self.cur_user))
            check2 = cursor.fetchall() != []
            if check2:
                QMessageBox.about(self, "Неверные даннные", "Модифиц. контакт уже существует")
                return
            if check1 and (not check2):
                self.got_signal.emit("{};{};{};{};{};{}".format(name, phone, final_birth_day, name2, phone2, final_birth_day2))
                self.close()
        cursor.close()
        conn.close()

