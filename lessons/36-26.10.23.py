# import sqlite3

# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
    # cur.execute('''
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT "+79090000000",
    # age INTEGER CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )''')
    # cur.execute('''
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT;
    # ''')
    # cur.execute('''
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;
    # ''')
    # cur.execute('''
    # ALTER TABLE person_table
    # DROP COLUMN home_address;
    # ''')
    # cur.execute('''
    # DROP TABLE person_table
    # ''')


# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute('''
#         SELECT *
#         FROM T1
#         ORDER BY FName
#         LIMIT 2, 5
#     ''')
#
#     # res = cur.fetchall()  # => [(), ()]
#     # print(res)
#
#     # for res in cur:
#     #     print(res)
#
#     res = cur.fetchone()  # => ()
#     print(res)
#     res2 = cur.fetchmany(2)  # => [(), ()]
#     print(res2)
#     res3 = cur.fetchall()  # => [(), ()]
#     print(res3)


import sqlite3

cars = [
    ('BMW', 54000),
    ('Chevrolet', 46000),
    ('Daewoo', 38000),
    ('Citroen', 29000),
    ('Honda', 33000)
]


with sqlite3.connect('car.db') as con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )''')

    cur.executescript('''
    DELETE FROM cars WHERE model LIKE "B%"; 
    UPDATE cars SET price = price + 100;
    ''')

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)

    # for car in cars:
    #     cur.execute('INSERT INTO cars VALUES(NULL, ?, ?)', car)

    # cur.execute('INSERT INTO cars VALUES(1, "Renault", 22000)')
    # cur.execute('INSERT INTO cars VALUES(2, "Volvo", 29000)')
    # cur.execute('INSERT INTO cars VALUES(3, "Mercedes", 57000)')
    # cur.execute('INSERT INTO cars VALUES(4, "Bentley", 35000)')
    # cur.execute('INSERT INTO cars VALUES(5, "Audi", 52000)')

# con.commit()
# con.close()




