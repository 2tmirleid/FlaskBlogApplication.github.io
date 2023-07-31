import flask
from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'akslkflsmflslsnflsfls'

menu = [{"name": "Установка", "url": "#"},
        {"name": "Первое приложение", "url": "#"},
        {"name": "Обратная связь", "url": "/contact"}]


@app.route("/")
def index():
    print(url_for("index"))
    return render_template("rkkindex.html", title="Главная", menu=menu)


# 19 str
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено!')
        else:
            flash('Введите корректное имя')

        print(request.form['username'], request.form['email'], request.form['message'])
    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route("/test/<username>")
def test(username):
    return f'Пользователь: {username}'


if __name__ == "__main__":
    app.run(debug=True)
