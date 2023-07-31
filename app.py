from flask import *

app = Flask(__name__)

menu = [{"name": "Установка", "url": "#"},
        {"name": "Первое приложение", "url": "#"},
        {"name": "Обратная связь", "url": "/contact"}]


@app.route("/")
def index():
    print(url_for("index"))
    return render_template("index.html", title="Главная", menu=menu)

#Added 19 string
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form['username'], request.form['email'], request.form['message'])

    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route("/test/<username>")
def test(username):
    return f'Пользователь: {username}'


if __name__ == "__main__":
    app.run(debug=True)
