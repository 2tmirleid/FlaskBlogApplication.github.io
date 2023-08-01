from flask import *
import sqlite3
import os

from db_settings import *

app = Flask(__name__)

menu = [{"name": "Установка", "url": "#"},
        {"name": "Первое приложение", "url": "#"},
        {"name": "Обратная связь", "url": "/contact"},
        {"name": "Авторизация", "url": "/login"}]


@app.route("/")
def index():
    db = get_db()
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено!', category='success')
        else:
            flash('Введите корректное имя', category='error')

        print(request.form['username'], request.form['email'], request.form['message'])
    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return render_template('profile.html', name=username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == '2tmirleid' and request.form['pass'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title="Страница не найдена", menu=menu), 404


@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html', title="Не авторизован", menu=menu), 401


@app.route("/test/<username>")
def test(username):
    return f'Пользователь: {username}'


if __name__ == "__main__":
    app.run(debug=True)
