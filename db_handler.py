# coding=utf-8
import mysql.connector as mariadb


class db_work():
    def __init__(self):
        self.conn = mariadb.connect(user='root', password='root', host='localhost', port='3306', autocommit=True)
        self.cursor = self.conn.cursor()
        self.cursor.execute("use test;")
        self.cursor.execute("""
        create table if not exists last_user(user_id integer);""")
        self.cursor.execute("""
        create table IF NOT EXISTS users (user_id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, 
        login VARCHAR(30), 
        password VARCHAR(30),
        birthday datetime);
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
        contact_id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR(30),
        phone_number VARCHAR(30),
        birthday datetime,
        user_id INTEGER,
        CONSTRAINT `fk_user`
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE
        ON UPDATE RESTRICT)      
        """)

    def auth(self, login, passwd):
        self.cursor.execute("select * from users where  login='{}' and password='{}';".format(login, passwd))
        return self.cursor.fetchall()

    def fill(self, user_id):
        self.cursor.execute("insert into last_user(user_id) values ({});".format(user_id))

    def check(self):
        self.cursor.execute("select * from last_user")
        return self.cursor.fetchall()
