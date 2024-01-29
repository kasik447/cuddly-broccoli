from flask import Flask, render_template, url_for, request, flash, g
import os
import sqlite3
from hw.flskdz.FDataBase import FDataBase


DATABASE = 'flskhw.db'
DEBUG = True
SECRET_KEY = '6ffca593e3ca0f26b30e024b68aff8a9999aee6c'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, "flskhw.db")))


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {"name": "Главная", "url": "index"},
    {"name": "Адреса магазинов", "url": "addresses"},
    {"name": "Интернет магазин", "url": "shops"},
    {"name": "Стать партнёром", "url": "partners"},
    {"name": "Авторизация", "url": "username"}
]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


# @app.route("/index")
@app.route("/")
def index():
    # print(url_for("index"))
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu())


@app.route("/addresses")
def addresses():
    # print(url_for("addresses"))
    db = get_db()
    dbase = FDataBase(db)
    return render_template("addresses.html", title="Адреса магазинов", menu=dbase.get_menu())


@app.route("/shops")
def shops():
    # print(url_for("shops"))
    db = get_db()
    dbase = FDataBase(db)
    return render_template("shops.html", title="Интернет магазин", menu=dbase.get_menu())


@app.route("/partners")
def partners():
    # print(url_for("partners"))
    db = get_db()
    dbase = FDataBase(db)
    return render_template("partners.html", title="Стать партнёром", menu=dbase.get_menu())


@app.route("/username")
def username():
    # print(url_for("username"))
    db = get_db()
    dbase = FDataBase(db)
    return render_template("username.html", title="Авторизация", menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
