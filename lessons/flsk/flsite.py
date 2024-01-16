from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route("/index")
@app.route("/")
def index():
    print(url_for("index"))  # /
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/about")
def about():
    print(url_for("about"))  # /about
    return render_template("about.html", title="О нас", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
        # print(request.form["username"])
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        return render_template("shops.html", **context, title="Обратная связь", menu=menu)
    return render_template("shops.html", title="Обратная связь", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
