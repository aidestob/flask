from flask import Flask, redirect, url_for, render_template
from db import init_db, db_session
from form import AddPost
from models import User, Posts
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'uhewfquiwghefipuhcwueuhcq+ow34hm-98eoiajsdoi_fj,aspodm'
init_db()
bootstrap = Bootstrap(app)


def addtodb(obj):
  db_session.add(obj)
  db_session.commit()

@app.route('/')
def index():
  '''
  Обработчик главной страницы.
  Получаем все посты из базы и передаем в шаблон
  '''
  posts=Posts.query.all()
  return render_template('index.html', posts=posts)


@app.route('/addpost', methods=['GET', 'POST'])
def addpost():
  '''
  Обработчик страницы добавления поста.
  Два поля имя пользователя и текст поста
  являются обязательными, наличие текста проверяется
  валидатором в форме. В случае отсутствия значения в поле,
  пользователю будет предоставлено предупреждение.
  '''
  form = AddPost()
  if form.validate_on_submit():
    username = form.username.data
    post = form.post.data
    #Отбираем из базы пользователя
    user = User.query.filter(User.username == username).first()
    if not user:
      #Если его не существует, переопределяем переменную и создаем пользователя.
      user = User(username, f"{username}@mail.ru")
      addtodb(user)
    obj = Posts(user, post)
    addtodb(obj)
    return redirect(url_for('index'))
  return render_template('addpost.html', title='Add Post', form=form)


@app.route('/user/<username>')
def show_user_profile(username):
  '''
  Обработчик страницы пользователя.
  Отображает все посты конкретного пользователя.
  '''
  user = User.query.filter(User.username == username).first()
  posts = user.posts
  return render_template('user.html', posts=posts, username=user.username)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == 'main':
  app.run(debug=True)