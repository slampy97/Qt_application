# coding=utf-8
from PyQt5 import QtWidgets, QtGui, QtCore, uic
import mysql.connector as mariadb
import sys

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QDialog, QLineEdit, QTableWidgetItem, QStyle, QMessageBox, QPushButton

from add_contact import WorkWithContact

class TableContacts(QtWidgets.QDialog):
    got_signal = pyqtSignal(str)

    def On_buttonclick_clicked(self):
        self.setVisible(False)
        self.got_signal.emit("something")

    def __init__(self, cur_user, flags=None, *args, **kwargs):
        QDialog.__init__(self, flags, *args, **kwargs)
        self.cur_user = cur_user
        self.resize(470, 507)
        total_layout = QtWidgets.QVBoxLayout()
        self.setLayout(total_layout)
        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.West)
        total_layout.addWidget(self.tab_widget)
        self.tab1 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab1, "AБ")
        self.tab2 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab2, "ВГ")
        self.tab3 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab3, "ДЕ")
        self.tab4 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab4, "ЖЗИЙ")
        self.tab5 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab5, "КЛ")
        self.tab6 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab6, "МН")
        self.tab7 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab7, "ОП")
        self.tab8 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab8, "РС")
        self.tab9 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab9, "ТУ")
        self.tab10 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab10, "ФХ")
        self.tab11 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab11, "ЦЧШЩ")
        self.tab12 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab12, "ЬЫЪЭ")
        self.tab13 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab13, "ЮЯ")
        self.tab14 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab14, "other")

        tab1_layout = QtWidgets.QHBoxLayout(self.tab1)
        self.tabl_tab1 = QtWidgets.QTableWidget()
        tab1_layout.addWidget(self.tabl_tab1)
        self.fill_table(u"аб", self.tabl_tab1)

        self.tabl_tab2 = QtWidgets.QTableWidget()
        tab2_layout = QtWidgets.QHBoxLayout(self.tab2)
        tab2_layout.addWidget(self.tabl_tab2)
        self.fill_table(u"вг", self.tabl_tab2)

        tab3_layout = QtWidgets.QHBoxLayout(self.tab3)
        self.tabl_tab3 = QtWidgets.QTableWidget()
        tab3_layout.addWidget(self.tabl_tab3)
        self.fill_table(u"де", self.tabl_tab3)

        tab4_layout = QtWidgets.QHBoxLayout(self.tab4)
        self.tabl_tab4 = QtWidgets.QTableWidget()
        tab4_layout.addWidget(self.tabl_tab4)
        self.fill_table(u"жзий", self.tabl_tab4)

        tab5_layout = QtWidgets.QHBoxLayout(self.tab5)
        self.tabl_tab5 = QtWidgets.QTableWidget()
        tab5_layout.addWidget(self.tabl_tab5)
        self.fill_table(u"кл", self.tabl_tab5)

        tab6_layout = QtWidgets.QHBoxLayout(self.tab6)
        self.tabl_tab6 = QtWidgets.QTableWidget()
        tab6_layout.addWidget(self.tabl_tab6)
        self.fill_table(u"мн", self.tabl_tab6)

        tab7_layout = QtWidgets.QHBoxLayout(self.tab7)
        self.tabl_tab7 = QtWidgets.QTableWidget()
        tab7_layout.addWidget(self.tabl_tab7)
        self.fill_table(u"оп", self.tabl_tab7)

        tab8_layout = QtWidgets.QHBoxLayout(self.tab8)
        self.tabl_tab8 = QtWidgets.QTableWidget()
        tab8_layout.addWidget(self.tabl_tab8)
        self.fill_table(u"рс", self.tabl_tab8)

        tab9_layout = QtWidgets.QHBoxLayout(self.tab9)
        self.tabl_tab9 = QtWidgets.QTableWidget()
        tab9_layout.addWidget(self.tabl_tab9)
        self.fill_table(u"ту", self.tabl_tab9)

        tab10_layout = QtWidgets.QHBoxLayout(self.tab10)
        self.tabl_tab10 = QtWidgets.QTableWidget()
        tab10_layout.addWidget(self.tabl_tab10)
        self.fill_table(u"фх", self.tabl_tab10)

        tab11_layout = QtWidgets.QHBoxLayout(self.tab11)
        self.tabl_tab11 = QtWidgets.QTableWidget()
        tab11_layout.addWidget(self.tabl_tab11)
        self.fill_table(u"цчшщ", self.tabl_tab11)

        tab12_layout = QtWidgets.QHBoxLayout(self.tab12)
        self.tabl_tab12 = QtWidgets.QTableWidget()
        tab12_layout.addWidget(self.tabl_tab12)
        self.fill_table(u"ьэыъ", self.tabl_tab12)

        tab13_layout = QtWidgets.QHBoxLayout(self.tab13)
        self.tabl_tab13 = QtWidgets.QTableWidget()
        tab13_layout.addWidget(self.tabl_tab13)
        self.fill_table(u"юя", self.tabl_tab13)

        tab14_layout = QtWidgets.QHBoxLayout(self.tab14)
        self.tabl_tab14 = QtWidgets.QTableWidget()
        tab14_layout.addWidget(self.tabl_tab14)
        self.fill_table(u"other", self.tabl_tab14)

        self.btn_layout = QtWidgets.QHBoxLayout()
        total_layout.addLayout(self.btn_layout)
        self.btn1 = QtWidgets.QPushButton()
        self.btn1.setText("Добавить контакт")
        self.btn_layout.addWidget(self.btn1)
        self.btn1.clicked.connect(self.add_contact)
        self.btn2 = QtWidgets.QPushButton()
        self.btn2.setText("Удаление контакта")
        self.btn_layout.addWidget(self.btn2)
        self.btn2.clicked.connect(self.del_contact)
        self.btn3 = QtWidgets.QPushButton()
        self.btn3.setText("Модифиц. контакт")
        self.btn3.clicked.connect(self.modify_contact)
        self.btn_layout.addWidget(self.btn3)
        self.btn_dr = QPushButton()
        self.btn_dr.setText("Др")
        self.btn_dr.clicked.connect(self.notification)


    def notification(self):
        conn = mariadb.connect(user='root', password='root', host='localhost', port='3306', autocommit=True)
        cursor = conn.cursor()
        cursor.execute("use test;")
        cursor.execute("select name from contacts where  (dayofyear(birthday) between dayofyear(now()) and dayofyear(now() + interval 7 day)) and user_id={}; ".format(self.cur_user))
        records = cursor.fetchall()
        final_msg = "Скоро ДР У:"
        for record in records:
            final_msg += "\n" + record[0].encode('utf-8')
        QMessageBox.about(self, "ДР", final_msg)

    def modify_contact(self):
        modify = WorkWithContact(self.cur_user, 2)
        modify.show()
        modify.got_signal.connect(self.handle3)
        modify.exec_()

    def add_contact(self):
        add_contact = WorkWithContact(self.cur_user, 0)
        add_contact.show()
        add_contact.got_signal.connect(self.handle)
        add_contact.exec_()

    def del_contact(self):
        delete_contact = WorkWithContact(self.cur_user, 1)
        delete_contact.show()
        delete_contact.got_signal.connect(self.handle2)
        delete_contact.exec_()

    def handle2(self, signal):
        name, phone, birthday = signal.split(";")
        name = name.encode('utf-8')
        phone = phone.encode('utf-8')
        birthday = birthday.encode('utf-8')
        conn = mariadb.connect(user='root', password='root', host='localhost', port='3306', autocommit=True)
        cursor = conn.cursor()
        cursor.execute("use test;")
        cursor.execute(
            "delete from contacts where name=\"{}\" and phone_number=\"{}\" and birthday=\"{}\" and user_id={};".format(
                name, phone, birthday, self.cur_user))

        self.find_and_delete_row(name, phone, birthday)
        cursor.close()
        conn.close()

    def handle3(self, signal):
        name, phone, birthday, name2, phone2, birthday2 = signal.split(";")
        name = name.encode('utf-8')
        phone = phone.encode('utf-8')
        birthday = birthday.encode('utf-8')
        name2 = name2.encode('utf-8')
        phone2 = phone2.encode('utf-8')
        birthday2 = birthday2.encode('utf-8')
        conn = mariadb.connect(user='root', password='root', host='localhost', port='3306', autocommit=True)
        cursor = conn.cursor()
        cursor.execute("use test;")
        cursor.execute(
            "delete from contacts where name=\"{}\" and phone_number=\"{}\" and birthday=\"{}\" and user_id={};".format(
                name, phone, birthday, self.cur_user))
        cursor.execute(
            "insert into contacts(contacts.name, contacts.phone_number, contacts.birthday, contacts.user_id) values (\"{}\",\"{}\",\"{}\",\"{}\")".format(
                name2, phone2, birthday2, self.cur_user))

        self.find_and_delete_row(name, phone, birthday)
        self.send_message(name2, phone2, birthday2)

    def send_message(self, name, phone, birthday):
        res = ""
        if name.startswith('а') or name.startswith('б'):
            table = self.tabl_tab1
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "аб"
        elif name.startswith('в') or name.startswith('г'):
            table = self.tabl_tab2
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "вг"
        elif name.startswith('д') or name.startswith('е'):
            table = self.tabl_tab3
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "де"
        elif name.startswith('ж') or name.startswith('з') or name.startswith('и') or name.startswith('й'):
            table = self.tabl_tab4
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "жзий"
        elif name.startswith('к') or name.startswith('л'):
            table = self.tabl_tab5
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "кл"
        elif name.startswith('м') or name.startswith('н'):
            table = self.tabl_tab6
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "мн"
        elif name.startswith('о') or name.startswith('п'):
            table = self.tabl_tab7
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "оп"
        elif name.startswith('р') or name.startswith('с'):
            table = self.tabl_tab8
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "рс"
        elif name.startswith('т') or name.startswith('у'):
            table = self.tabl_tab9
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "ту"
        elif name.startswith('ф') or name.startswith('х'):
            table = self.tabl_tab10
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "фх"
        elif name.startswith('ц') or name.startswith('ч') or name.startswith('ш') or name.startswith('щ'):
            table = self.tabl_tab11
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "цчшщ"
        elif name.startswith('э') or name.startswith('ы') or name.startswith('ь') or name.startswith('ъ'):
            table = self.tabl_tab12
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "эыъь"
        elif name.startswith('а') or name.startswith('я'):
            table = self.tabl_tab13
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "ая"
        else:
            table = self.tabl_tab14
            self.add_contact_to_Table(table, name, phone, birthday)
            res = "other"

        QMessageBox.about(self, "Модификация контакта", "[Моциф.]Контакт добавлен в раздел {}".format(res))

    def find_table(self, name):
        if name.startswith('а') or name.startswith('б'):
            return self.tabl_tab1
        elif name.startswith('в') or name.startswith('г'):
            return self.tabl_tab2
        elif name.startswith('д') or name.startswith('е'):
            return self.tabl_tab3
        elif name.startswith('ж') or name.startswith('з') or name.startswith('и') or name.startswith('й'):
            return self.tabl_tab4
        elif name.startswith('к') or name.startswith('л'):
            return self.tabl_tab5
        elif name.startswith('м') or name.startswith('н'):
            return self.tabl_tab6
        elif name.startswith('о') or name.startswith('п'):
            return self.tabl_tab7
        elif name.startswith('р') or name.startswith('с'):
            return self.tabl_tab8
        elif name.startswith('т') or name.startswith('у'):
            return self.tabl_tab9
        elif name.startswith('ф') or name.startswith('х'):
            return self.tabl_tab10
        elif name.startswith('ц') or name.startswith('ч') or name.startswith('ш') or name.startswith('щ'):
            return self.tabl_tab11
        elif name.startswith('э') or name.startswith('ы') or name.startswith('ь') or name.startswith('ъ'):
            return self.tabl_tab12
        elif name.startswith('а') or name.startswith('я'):
            return self.tabl_tab13
        else:
            return self.tabl_tab14

    def find_and_delete_row(self, name, phone, birthday):
        table = self.find_table(name)
        row_number = table.rowCount()
        for i in range(row_number):
            name_i = table.item(i, 0).text().encode('utf-8')
            phone_i = table.item(i, 1).text().encode('utf-8')
            birthday_i = table.item(i, 2).text().encode('utf-8')
            if name_i == name and phone_i == phone and birthday_i == birthday:
                table.removeRow(i)
                break

    def handle(self, signal):
        name, phone, birthday = signal.split(";")
        name = name.encode('utf-8')
        phone = phone.encode('utf-8')
        birthday = birthday.encode('utf-8')
        conn = mariadb.connect(user='root', password='root', host='localhost', port='3306', autocommit=True)
        cursor = conn.cursor()
        cursor.execute("use test;")
        cursor.execute(
            "insert into contacts(name, phone_number, birthday, user_id) values (\"{}\",\"{}\",\"{}\",\"{}\")".format(
                name, phone, birthday, self.cur_user))
        cursor.close()
        conn.close()
        self.send_message(name, phone, birthday)

    def add_contact_to_Table(self, table, name, phone, birthday):
        item = QtWidgets.QTableWidgetItem(name)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        last = table.rowCount()
        table.insertRow(last)
        table.setItem(last, 0, item)
        item = QtWidgets.QTableWidgetItem(phone)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        table.setItem(last, 1, item)
        item = QtWidgets.QTableWidgetItem(birthday)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        table.setItem(last, 2, item)

    def fill_table(self, array_of_sym, table):
        conn = mariadb.connect(user='root', password='root', host='localhost', port='3306')
        cursor = conn.cursor()
        cursor.execute("use test;")
        res = []
        for sym in array_of_sym:
            cursor.execute(
                "select name, phone_number, birthday from contacts where contacts.name like \"{}%\" and contacts.user_id ={} ".format(
                    sym.encode('utf-8'), self.cur_user))
            for el in cursor.fetchall():
                res.append(el)
        table.setRowCount(len(res))
        table.setColumnCount(3)
        table.setHorizontalHeaderItem(0, QTableWidgetItem("Имя"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("Телефон"))
        table.setHorizontalHeaderItem(2, QTableWidgetItem("Дата рождения"))
        i = 0
        for record in res:
            name = record[0].encode('utf-8')
            phone_number = record[1].encode('utf-8')
            birth_date = "{}-{}-{}".format(record[2].year, record[2].month, record[2].day)
            item = QtWidgets.QTableWidgetItem(name)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem(phone_number)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem(birth_date)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.setItem(i, 2, item)
            i += 1
        cursor.close()
        conn.close()

