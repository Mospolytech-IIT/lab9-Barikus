"""Взаимодействие с базой данных"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post
from engine import get_engine

def add_data(session):
    """Добавление"""
    # Добавление пользователей
    user1 = User(username='user1', email='user1@mail.ru', password='password1')
    user2 = User(username='user2', email='user2@mail.ru', password='password2')
    session.add_all([user1, user2])
    session.commit()

    # Добавление постов
    post1 = Post(title='Post1', content='Hello Hello', user_id=user1.id)
    post2 = Post(title='Post2', content='Goodbye Goodbye', user_id=user2.id)
    session.add_all([post1, post2])
    session.commit()

def get_data(session):
    """Получение""" 
    # Получение всех пользователей
    users = session.query(User).all()
    for user in users:
        print(user.username, user.email)

    # Получение всех постов с информацией о пользователях
    posts = session.query(Post).join(User).all()
    for post in posts:
        print(post.title, post.content, post.user.username)

    # Получение постов конкретного пользователя
    specific_user_posts = session.query(Post).filter_by(user_id=1).all()
    for post in specific_user_posts:
        print(post.title, post.content, post.user.username)

def update_data(session):
    """Обновление""" 
    # Обновление email пользователя
    user1 = session.query(User).filter_by(id=1).first()
    user1.email = 'new_email@mail.com'
    session.commit()

    # Обновление content поста
    post1 = session.query(Post).filter_by(id=1).first()
    post1.content = 'Updated conte  nt'
    session.commit()

def delete_data(session):
    """Удаление"""
    # Удаление одного из постов
    post = session.query(Post).filter_by(id=1).first()
    session.delete(post)
    session.commit()

    # Удаление пользователя и всех его постов
    user = session.query(User).filter_by(id=1).first()
    session.delete(user)
    session.commit()

if __name__ == "__main__":
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    my_session = Session()

    add_data(my_session)
    get_data(my_session)
    update_data(my_session)
    delete_data(my_session)
