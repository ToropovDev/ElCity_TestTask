import sqlite3

values_td = [(111111, 1, "ВЛ", False, None),
(222222, 2, "ВЛ", False, None),
(222222, 3, "ДМФ", False, None),
(222222, 4, "IPTV", False, None),
(222222, 5, "IPTV", True, None),
(222222, 6, "Видеосервис", True, None),
(222222, 7, "Видеосервис", True, None),
(222222, 8, "Оборудование", True, None),
(222222, 9, "КТВ", False, None),
(222222, 10, "Оборудование", True, None),
(222222, 11, "Оборудование", True, None),
(333333, 12, "ВЛ", False, 888),
(333333, 888, "Пакет", False, None),
(333333, 13, "IPTV", False, 888),
(333333, 14, "IPTV", False, 888),
(333333, 15, "IPTV", False, 888),
(333333, 16, "IPTV", False, 888),
(333333, 17, "Оборудование", False, None),
(333333, 18, "КТВ", False, None)]

values_email = [(111111, "111111@mail.ru"),
(333333, "333333@mail.ru")]

conn = sqlite3.connect('database.db')
cur = conn.cursor()


def create_tables():

    cur.execute('''CREATE TABLE IF NOT EXISTS TD (
                 doc_num INTEGER,
                 code_TD INTEGER,
                 service TEXT,
                 deleted BOOLEAN,
                 link INTEGER
                 )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS email (
                 doc_num INTEGER,
                 email TEXT
                 )''')

    conn.commit()


def fill_tables():
    cur.executemany('''INSERT INTO TD (doc_num, code_TD, service, deleted, link) VALUES (?,?,?,?,?)''', values_td)
    cur.executemany('''INSERT INTO email (doc_num, email) VALUES (?,?)''', values_email)

    conn.commit()


