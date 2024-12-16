"""Файл для подключения к БД"""
from sqlalchemy import create_engine

def get_engine():
    """Возвращает engine для подключения"""
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres2"
    engine = create_engine(DATABASE_URL)
    return engine
