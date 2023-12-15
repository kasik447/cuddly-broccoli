import sqlite3

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


with sqlite3.connect("db_3.db") as con:
    cur = con.cursor()
    cur.execute('''
        SELECT *
        FROM T1 
        ORDER BY FName
        LIMIT 2, 5
    ''')

    # res = cur.fetchall()  # => [(), ()]
    # print(res)

    # for res in cur:
    #     print(res)

    res = cur.fetchone()  # => ()
    print(res)
    res2 = cur.fetchmany(2)  # => [(), ()]
    print(res2)
    res3 = cur.fetchall()  # => [(), ()]
    print(res3)




