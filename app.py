from flask import *
import sqlite3
import os
import db_settings
from db_settings import *
import FDataBase
from FDataBase import *

app = Flask(__name__)
app.secret_key = db_settings.SECRET_KEY


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Главная", menu=dbase.getMenu(), posts=dbase.getPostsAnnounce())


@app.route("/add_post", methods=['POST', 'GET'])
def addPost():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'])
            if not res:
                flash('Ошибка при добавлении статьи', category='error')
            else:
                flash('Статья успешно добавлена', category='success')
        else:
            flash('Ошибка при добавлении статьи', category='error')

    return render_template('add_post.html', menu=dbase.getMenu(), title='Добавление статьи')


@app.route("/post/<int:id_post>")
def showPost(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(id_post)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('404.html', title="Страница не найдена", menu=dbase.getMenu()), 404


@app.errorhandler(401)
def unauthorized(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('401.html', title="Не авторизован", menu=dbase.getMenu()), 401


if __name__ == "__main__":
    app.run(debug=False)
