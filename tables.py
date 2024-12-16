"""Таблицы"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    "Таблица пользователя"
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    posts = relationship('Post', back_populates='user')

class Post(Base):
    "Таблица постов"
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='posts')

if __name__ == "__main__":
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres2"
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
