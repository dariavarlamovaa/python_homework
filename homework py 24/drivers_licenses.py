# 1. Создайте некоторую базу данных, используя sqlite3.
# 2. В ней реализуйте 2-3 таблицы, при создании которых используйте различные ограничения и типы данных столбцов.
# 3. После этого наполните таблицу разными данными, используя разные варианты(например, введенные данные вручную, данные из какого-то файла и т.д.)
# 4. Также, не забудьте открыть эту базу данных в SQLiteStudio и проверить все свойства. После чего попробуйте написать несколько запросов, использующих связи между таблицами.


# import sqlite3 as sq
# import json
#
# ------------------------ task 1 - Create Database ------------------------
# with sq.connect('drivers_licenses.db') as con:
#     cur = con.cursor()
#     ------------------------ task 2 - Create tables ------------------------
#     cur.execute('''CREATE TABLE IF NOT EXISTS drivers(
#                 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL CHECK(name!=''),
#                 date_of_birth TEXT NOT NULL
#                 )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS licenses(
#                 license_id INTEGER PRIMARY KEY UNIQUE,
#                 user_id INTEGER,
#                 issue_date TEXT NOT NULL,
#                 FOREIGN KEY(user_id) REFERENCES drivers(user_id)
#                 )''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS violations(
#                 violation_id INTEGER PRIMARY KEY,
#                 license_id INTEGER,
#                 violation_date TEXT,
#                 FOREIGN KEY(license_id) REFERENCES licenses(license_id)
#                 )''')
#
#     ------------------------ task 3 - Insert values ------------------------
#     -------- insert with many rows --------
#
#     cur.execute('''INSERT INTO drivers VALUES(NULL, "Alex", "23.09.2000")''')
#     cur.execute('''INSERT INTO drivers VALUES(NULL, "Leo", "20.04.1999")''')
#     cur.execute('''INSERT INTO drivers VALUES(NULL, "Eliot", "12.10.1998")''')
#     cur.execute('''INSERT INTO drivers VALUES(NULL, "Peter", "29.12.1990")''')
#     cur.execute('''INSERT INTO drivers VALUES(NULL, "Christopher", "12.01.2001")''')
#
#     -------- insert with executemany() --------
#
#     licenses_info = [
#         (90345, 1, "21.04.2022"),
#         (34543, 3, "23.04.2022"),
#         (22234, 5, "24.04.2022"),
#         (23423, 4, "26.04.2022"),
#         (12322, 2, "28.04.2022")
#     ]
#
#     cur.executemany('''INSERT INTO licenses VALUES(?, ?, ?)''', licenses_info)
#
#     -------- insert from json-file --------
#
#     with open('violations.json', 'r') as v:
#         violations_info = json.load(v)
#     for violation in violations_info:
#         violation_id = violation['Violation ID']
#         license_id = violation['License ID']
#         violation_date = violation['Violation Date']
#         cur.execute('''INSERT INTO violations VALUES(?, ?, ?)''', (violation_id, license_id, violation_date))
# 
#     con.commit()
#
#     ------------------------ task 4 - Write SQL-queries ------------------------
#
#     cur.execute('''
#                 SELECT d.name, l.issue_date
#                 FROM Licenses l, Drivers d, Violations v
#                 WHERE d.user_id = l.user_id and l.license_id = v.license_id and v.violation_date LIKE "1_.03.2022"
#                 ''')
#     print(cur.fetchall())
#
#     cur.execute('''
#                 SELECT v.violation_date, l.user_id, d.name
#                 FROM Violations v, Licenses l, Drivers d
#                 WHERE v.license_id = l.license_id and l.user_id = d.user_id
#                 ''')
#     print(cur.fetchall())
