from database import create_tables, fill_tables, cur, conn


def print_list(l):
    for elem in l:
        print(elem)
    print()


create_tables()
fill_tables()

# 1 -
cur.execute("SELECT DISTINCT doc_num FROM TD")
unique_numbers = cur.fetchall()
print("1. Вывести уникальные номера договоров из таблицы ТД")
print_list(unique_numbers)

# 2
cur.execute("SELECT * FROM TD WHERE service = 'Оборудование'")
equipment_rows = cur.fetchall()
print("2. Вывести таблицу ТД, только с оборудованием")
print_list(equipment_rows)

# 3
cur.execute("""
    SELECT t1.doc_num, t1.code_TD AS Код_ТД_Пакета, t2.code_TD AS Код_ТД, t2.service AS Услуга
    FROM TD t1
    JOIN TD t2 ON t1.doc_num = t2.doc_num AND t1.link = t2.code_TD
    """)
package_rows = cur.fetchall()
print("3. Вывести все ТД, которые входят в пакет Формат: Номер договора, Код ТД Пакета, Код ТД, Услуга")
print_list(package_rows)

# 4
cur.execute("""
    SELECT TD.*, email.email
    FROM TD
    LEFT JOIN email ON TD.doc_num = email.doc_num
    """)
td_rows_with_email = cur.fetchall()
print("4. Вывести всю таблицу с ТД с E-mail абонента")
print_list(td_rows_with_email)

# 5
cur.execute("""
    SELECT TD.*
    FROM TD
    LEFT JOIN email ON TD.doc_num = email.doc_num
    WHERE email.doc_num IS NULL
    """)
td_rows_without_email = cur.fetchall()
print("5. Вывести только тех абонентов, у которых нет E-mail")
print_list(td_rows_without_email)

# 6
cur.execute("""
    SELECT doc_num, 
           GROUP_CONCAT(code_TD) AS Код_ТД, 
           GROUP_CONCAT(service) AS Услуги
    FROM TD
    WHERE NOT deleted
    GROUP BY doc_num
    """)
active_services_rows = cur.fetchall()
print("6. Вывести таблицу ТД с действующими услугами в следующем формате: Номер договора, массив из Код ТД, массив из услуг")
print_list(active_services_rows)

# 8
cur.execute("""
    WITH td_with_email AS (
        SELECT TD.*, email.email
        FROM TD
        LEFT JOIN email ON TD.doc_num = email.doc_num
    )
    SELECT * FROM td_with_email;
    """)
results = cur.fetchall()
print("8. Самопроизвольный код с использованием CTE на данных таблицах")
print_list(results)
