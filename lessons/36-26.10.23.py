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


# import sqlite3
#
# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
#
# with sqlite3.connect('car.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )''')

    # cur.executescript('''
    # DELETE FROM cars WHERE model LIKE "B%";
    # UPDATE cars SET price = price + 100;
    # ''')

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

# import sqlite3
#
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, "Renault", 22000);
#     UPDATE cars SET price = price + 200;
#     ''')
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса", e)
# finally:
#     if con:
#         con.close()


# import sqlite3
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#
#     return True
#
#
# with sqlite3.connect('car.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS users(
#     name TEXT,
#     ava BLOB,
#     score INTEGER
#     );''')
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#     write_ava("out.png", img)

    # img = read_ava(1)
    # if img:
    #     binary = sqlite3.Binary(img)
    #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))

    # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    # last_row_id = cur.lastrowid
    # buy_car_id = 2
    # cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

    # cur.execute("SELECT model, price FROM cars")
    #
    # row = cur.fetchone()
    # print(row)
    # row2 = cur.fetchmany(5)
    # print(row2)
    # row3 = cur.fetchall()
    # print(row3)
    # for res in cur:
    #     print(res['model'], "->", res['price'])


# import sqlite3
#
#
# with sqlite3.connect('car.db') as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


    # with open("sql_dump.sql", "w") as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    # for sql in con.iterdump():
    #     print(sql)


# SQLAlchemy ORM

# import os
#
# from lessons.modelsHW.database import DATABASE_NAME, Session
# import create_database1 as db_creator
#
# from lessons.models.lesson import Lesson, association_table
# from lessons.models.student import Student
# from lessons.models.group import Group
# from sqlalchemy import and_, or_, not_, desc
#
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
    # print(session.query(Lesson).all())
    # print('*' * 60)
    #
    # for it in session.query(Lesson):
    #     print(it)
    # print('*' * 60)
    #
    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print('*' * 60)
    #
    # print(session.query(Lesson).count())
    # print('*' * 60)
    #
    # print(session.query(Lesson).first())
    # print('*' * 60)
    #
    # for it in session.query(Lesson).filter(Lesson.id > 3):
    #     print(it)
    # print('*' * 60)
    #
    # for it in session.query(Lesson).filter(Lesson.id > 3, Lesson.lesson_title.like("Ф%")):
    #     print(it)
    # print('*' * 60)
    #
    # for it in session.query(Lesson).filter(or_(Lesson.id > 3, Lesson.lesson_title.like("Ф%"))):
    #     print(it)
    # print('*' * 60)
    #
    # for it in session.query(Lesson).filter(not_(Lesson.id > 3), not_(Lesson.lesson_title.like("Ф%"))):
    #     print(it)
    # print('*' * 60)
    #
    # for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(
    #         and_(association_table.c.lesson_id == Lesson.id,
    #              association_table.c.group_id == Group.id, Group.group_name == 'MDA-9')):
    #     print(it, gr)
    # print('*' * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
    # print('*' * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
    # print('*' * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all())
    # print('*' * 60)
    #
    # print(session.query(Student).filter(not_(Student.age.between(16, 17))).all())
    # print('*' * 60)
    #
    # for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
    #     print(it)
    # print('*' * 60)
    #
    # for it in session.query(Student).order_by(desc(Student.surname)):
    #     print(it)
    # print('*' * 60)
    #
    # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'):
    #     print(it)
    # print('*' * 60)

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print('*' * 60)
    #
    # i = session.query(Lesson).first()
    # i.lesson_title = "Информатика"
    # session.add(i)
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print('*' * 60)
    #
    # session.query(Lesson).filter(Lesson.lesson_title.like("%м%")).update(
    #     {"lesson_title": "М"}, synchronize_session='fetch')
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print('*' * 60)
    #
    # session.add(Lesson(lesson_title="Математика"))
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print('*' * 60)
    #
    # i = session.query(Lesson).filter(Lesson.lesson_title == "М").first()
    # session.delete(i)
    # session.commit()
    #
    # for it in session.query(Lesson):
    #     print(it.lesson_title)
    # print('*' * 60)

import os

from lessons.modelsHW.database import DATABASE_NAME
import create_database1 as db_creator


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()





