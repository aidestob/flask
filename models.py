from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
  '''
  Модель для расположения учетных записей
  пользователей. Создана связь one-to-many
  между таблицей users и posts.
  '''
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(80), unique=True, nullable=False)
  email = Column(String(120), unique=True, nullable=False)
  posts = relationship(
        "Posts",
        back_populates="author",
        cascade="all, delete",
        passive_deletes=True,
    )

  def __init__(self, username, email):
      self.username = username
      self.email = email

  def __repr__(self):
        return f'<User {self.username}>'


class Posts(Base):
  '''
  Модель для постов. Создана связь one-to-many
  между таблицей users и posts.
  '''
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
  author = relationship(
      "User",
      back_populates="posts"
  )
  title = Column(String(512), nullable=False)

  def __init__(self, author, title=None):
      self.author = author
      self.title = title

  def __repr__(self):
        return f'<Author {self.author.username}, Title: {self.title}>'


