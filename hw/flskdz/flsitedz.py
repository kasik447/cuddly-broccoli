from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "Адреса магазинов", "url": "addresses"},
    {"name": "Интернет магазин", "url": "shops"},
    {"name": "Стать партнёром", "url": "partners"},
    {"name": "Авторизация", "url": "username"}
]


@app.route("/index")
@app.route("/")
def index():
    print(url_for("index"))
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/addresses")
def addresses():
    print(url_for("addresses"))
    return render_template("addresses.html", title="Адреса магазинов", menu=menu)


@app.route("/shops")
def shops():
    print(url_for("shops"))
    return render_template("shops.html", title="Интернет магазин", menu=menu)


@app.route("/partners")
def partners():
    print(url_for("partners"))
    return render_template("partners.html", title="Стать партнёром", menu=menu)


@app.route("/username")
def username():
    print(url_for("username"))
    return render_template("username.html", title="Авторизация", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
