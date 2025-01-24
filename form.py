from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AddPost(FlaskForm):
  '''
  Форма добавления поста.
  Добавлены валидаторы на текстовые поля.
  '''
  username = StringField('Username', validators=[DataRequired()])
  post = TextAreaField('Post',  validators=[DataRequired()])
  submit = SubmitField('Add Post')