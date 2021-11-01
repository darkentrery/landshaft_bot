import sqlite3
import re
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(BASE_DIR, "clients_base.db")
password_base = os.path.join(BASE_DIR, "passwords.txt")
print(database)
print(password_base)


#database = "/usr/local/bin/landshaft_bot/clients_base.db"
#password_base = "/usr/local/bin/landshaft_bot/passwords.txt"

class Table():
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clients_base(
        user_id TEXT,
        password TEXT,
        name TEXT,
        phone TEXT,
        instagram TEXT,
        after_1 TEXT,
        h_w_1 TEXT,
        h_w_1_a TEXT,
        after_2 TEXT,
        h_w_2 TEXT,
        h_w_2_a TEXT,
        after_3 TEXT,
        h_w_3 TEXT,
        h_w_3_a TEXT,
        after_4 TEXT,
        h_w_4 TEXT,
        h_w_4_a TEXT,
        after_5 TEXT,
        h_w_5 TEXT,
        h_w_5_a TEXT,
        learn TEXT,
        tariff TEXT
        )""")
        self.conn.close()

    def delete_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS clients_base""")
        self.conn.close()

    def read_all(self):
        self.cursor.execute(f"SELECT * FROM clients_base")
        operations = self.cursor.fetchall()
        for i in range(len(operations)):
            print(operations[i])
        self.conn.close()

    def find_user(self, user_id):
        self.cursor.execute(f"SELECT user_id FROM clients_base WHERE user_id = '{user_id}'")
        user = self.cursor.fetchall()
        self.conn.close()
        return len(user)

    def connection(self, user_id):
        self.cursor.execute(f"INSERT INTO clients_base VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            user_id, 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False',
            'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False'))
        self.conn.commit()
        self.conn.close()

    #функция записывает в переменную name значение True для дальнейшей обработки
    def write_name_0(self, user_id):
        self.cursor.execute(f"UPDATE clients_base SET name = 'True' WHERE user_id = '{user_id}'")
        self.conn.commit()
        self.conn.close()

    #функция записывает в переменную password значение True для дальнейшей обработки
    def write_password_0(self, user_id):
        self.cursor.execute(f"UPDATE clients_base SET password = 'True' WHERE user_id = '{user_id}'")
        self.conn.commit()
        self.conn.close()

    # функция проверяет и записывает в переменную password значение пароля
    def write_password(self, user_id, password):
        w = False
        self.cursor.execute(f"SELECT password FROM clients_base WHERE user_id = '{user_id}'")
        password_0 = self.cursor.fetchall()[0][0]
        if password_0 == str(True):
            p1 = True #проверка отсутствия введенного пароля у других пользователей
            p2 = False #проверка наличия пароля в файле
            with open(password_base, 'r') as pas:
                passwords = pas.readlines()
            self.cursor.execute(f"SELECT password FROM clients_base")
            passwords_0 = self.cursor.fetchall()
            for p in range(len(passwords_0)):
                if password == passwords_0[p][0]:
                    p1 = False
                    break
            for p in range(len(passwords)):
                if password == passwords[p].strip():
                    p2 = True
                    break
            if p1 == True and p2 == True:
                self.cursor.execute(f"UPDATE clients_base SET password = '{password}' WHERE user_id = '{user_id}'")
                self.conn.commit()
                self.conn.close()
                w = True
            else:
                w = 2
        return w

    # функция записывает имя пользователя в базу данных
    def write_name(self, user_id, name):
        w = False
        self.cursor.execute(f"SELECT name FROM clients_base WHERE user_id = '{user_id}'")
        name_0 = self.cursor.fetchall()[0][0]
        textlookfor = r'\w{2,}\s\w{2,}'
        textlookfor_2 = r'\d'
        text = re.findall(textlookfor, str(name))
        text_2 = re.findall(textlookfor_2, str(name))
        #print(text, text_2, name.title())
        if name_0 == str(True):
            if len(text) == 1 and len(text_2) == 0:
                self.cursor.execute(f"UPDATE clients_base SET name = '{name.title()}' WHERE user_id = '{user_id}'")
                self.conn.commit()
                self.cursor.execute(f"UPDATE clients_base SET phone = 'True' WHERE user_id = '{user_id}'")
                self.conn.commit()
                w = True
            else:
                w = 2
        self.conn.close()
        return w

    # функция записывает номер телефона пользователя в базу данных
    def write_phone(self, user_id, phone):
        w = False
        self.cursor.execute(f"SELECT phone FROM clients_base WHERE user_id = '{user_id}'")
        phone_0 = self.cursor.fetchall()[0][0]
        textlookfor = [r'[\+]7\d{10}', r'8\d{10}']
        textlookfor_2 = r'\w'
        if phone_0 == str(True):
            text_2 = re.findall(textlookfor_2, str(phone))
            for t in range(len(textlookfor)):
                text = re.findall(textlookfor[t], str(phone))
                if len(text) == 1:
                    num = "8" + str(text[0])[len(text)-11:]
                    self.cursor.execute(f"UPDATE clients_base SET phone = '{num}' WHERE user_id = '{user_id}'")
                    self.conn.commit()
                    self.cursor.execute(f"UPDATE clients_base SET instagram = 'True' WHERE user_id = '{user_id}'")
                    self.conn.commit()
                    w = True
                    break
                else:
                    w = 2
        self.conn.close()
        return w

    # функция записывает инстаграм пользователя в базу данных
    def write_instagram(self, user_id, instagram):
        w = False
        self.cursor.execute(f"SELECT instagram FROM clients_base WHERE user_id = '{user_id}'")
        instagram_0 = self.cursor.fetchall()[0][0]
        if instagram_0 == str(True):
            print(instagram_0)
            self.cursor.execute(f"UPDATE clients_base SET instagram = '{instagram}' WHERE user_id = '{user_id}'")
            self.conn.commit()
            w = True
        self.conn.close()
        return w

    def write_after_0(self, user_id, i):
        after = 'after_' + str(i)
        self.cursor.execute(f"UPDATE clients_base SET {after} = 'True' WHERE user_id = '{user_id}'")
        self.conn.commit()
        self.conn.close()

    def write_after(self, user_id, i, after):
        w = False
        after_i = 'after_' + str(i)
        h_w = 'h_w_' + str(i)
        self.cursor.execute(f"SELECT {after_i} FROM clients_base WHERE user_id = '{user_id}'")
        after_0 = self.cursor.fetchall()[0][0]
        if after_0 == str(True):
            self.cursor.execute(f"UPDATE clients_base SET {after_i} = '{after}' WHERE user_id = '{user_id}'")
            self.conn.commit()
            self.cursor.execute(f"UPDATE clients_base SET {h_w} = 'True' WHERE user_id = '{user_id}'")
            self.conn.commit()
            w = True
        self.conn.close()
        return w

    def write_h_w(self, user_id, i, h_w_n):
        w = False
        h_w = 'h_w_' + str(i)
        self.cursor.execute(f"SELECT {h_w} FROM clients_base WHERE user_id = '{user_id}'")
        h_w_1_0 = self.cursor.fetchall()[0][0]
        if h_w_1_0 == str(True):
            self.cursor.execute(f"UPDATE clients_base SET {h_w} = '{h_w_n}' WHERE user_id = '{user_id}'")
            self.conn.commit()
            w = True
        self.conn.close()
        return w

    def write_h_w_a(self, user_id, i):
        h_w = 'h_w_' + str(i) + '_a'
        self.cursor.execute(f"SELECT {h_w} FROM clients_base WHERE user_id = '{user_id}'")
        h_w_a = self.cursor.fetchall()[0][0]
        if h_w_a == str(False):
            self.cursor.execute(f"UPDATE clients_base SET {h_w} = 'True' WHERE user_id = '{user_id}'")
            self.conn.commit()
        else:
            self.cursor.execute(f"UPDATE clients_base SET {h_w} = 'False' WHERE user_id = '{user_id}'")
            self.conn.commit()
        self.conn.close()

    def write_learn_0(self, user_id):
        self.cursor.execute(f"UPDATE clients_base SET learn = 'True' WHERE user_id = '{user_id}'")
        self.conn.commit()
        self.conn.close()

    def write_learn(self, user_id, learn):
        w = False
        self.cursor.execute(f"SELECT learn FROM clients_base WHERE user_id = '{user_id}'")
        learn_0 = self.cursor.fetchall()[0][0]
        if learn_0 == str(True):
            print(learn_0)
            self.cursor.execute(f"UPDATE clients_base SET learn = '{learn}' WHERE user_id = '{user_id}'")
            self.conn.commit()
            w = True
        self.conn.close()
        return w

    def write_tariff_0(self, user_id):
        self.cursor.execute(f"UPDATE clients_base SET tariff = 'True' WHERE user_id = '{user_id}'")
        self.conn.commit()
        self.conn.close()

    def write_tariff(self, user_id, tariff):
        w = False
        self.cursor.execute(f"SELECT tariff FROM clients_base WHERE user_id = '{user_id}'")
        tariff_0 = self.cursor.fetchall()[0][0]
        if tariff_0 == str(True):
            print(tariff_0)
            self.cursor.execute(f"UPDATE clients_base SET tariff = '{tariff}' WHERE user_id = '{user_id}'")
            self.conn.commit()
            w = True
        self.conn.close()
        return w

    def read_name(self, user_id):
        self.cursor.execute(f"SELECT name FROM clients_base WHERE user_id = '{user_id}'")
        name = self.cursor.fetchall()[0][0]
        return name

    def read_h_w(self, user_id, i):
        h_w = 'h_w_' + str(i)
        self.cursor.execute(f"SELECT {h_w} FROM clients_base WHERE user_id = '{user_id}'")
        h_w_1 = self.cursor.fetchall()[0][0]
        return h_w_1

    def read_h_w_a(self, user_id, i):
        h_w_a = 'h_w_' + str(i) + '_a'
        self.cursor.execute(f"SELECT {h_w_a} FROM clients_base WHERE user_id = '{user_id}'")
        h_w_1_a = self.cursor.fetchall()[0][0]
        return h_w_1_a

    def find_name(self, path):
        path = path.title()
        self.cursor.execute(f"SELECT name FROM clients_base")
        name = self.cursor.fetchall()
        names = []
        for i in range(len(name)):
            text = name[i][0]
            textlookfor = r'\b' + path + r'\b'
            namess = re.findall(textlookfor, text)
            if len(namess) != 0:
                names.append(text)
        print(name)
        return names

    def read_id(self, name):
        name = name.title()
        self.cursor.execute(f"SELECT user_id FROM clients_base WHERE name = '{name}'")
        user_id = self.cursor.fetchall()
        if len(user_id) != 0:
            user_id = user_id[0][0]
        else:
            user_id = None
        return user_id

    def read_ids(self):
        user_ids = []
        self.cursor.execute(f"SELECT user_id FROM clients_base ")
        user_id = self.cursor.fetchall()
        if len(user_id) != 0:
            for i in range(len(user_id)):
                user_ids.append(user_id[i][0])
        else:
            user_ids = None
        return user_ids

    def delete_str(self, user_id):
        self.cursor.execute(f"DELETE FROM clients_base WHERE user_id = '{user_id}'")
        self.conn.commit()
        self.conn.close()

#Table(database).create_table()
#Table(database).connection(1914280419)
#Table(database).write_password_0(1914280419)
#Table(database).write_password(1914280419, 'skldjg12njn3')
#Table(database).write_name_0(1914280419)
#Table(database).write_name(1914280419, 'Утебаева Марина')
#Table(database).write_phone(1914280419, '89276641669')
#Table(database).write_instagram(1914280419, '@greenastra')

#Table(database).connection(1560186607)
#Table(database).write_password_0(1560186607)
#Table(database).write_password(1560186607, 'ldkfg45kjknh')
#Table(database).write_name_0(1560186607)
#Table(database).write_name(1560186607, 'Наливайко Елена')
#Table(database).write_phone(1560186607, '89307117034')
#Table(database).write_instagram(1560186607, '@elen_nali')
#Table(database).read_all()

#Table(database).delete_table()
#Table(database).connection(4)
#Table(database).write_name(1, "True")
#Table(database).delete_str(1338438926)
#Table(database).read_all()
#Table(database).find_user("gyo")
#Table(database).write_password(3, '111')
