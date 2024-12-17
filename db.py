from sqlalchemy import create_engine  # сущность которая позволит запускать нашу БД
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# создаём engine для связи с нашей БД
engine = create_engine("sqlite:///ecommerce.db", echo=True)  # создали движок

# создаём сессию связи с нашей БД
SessionLocal = sessionmaker(bind=engine)  # bind - привязка и подтягиваем engine


# создаём класс будущей базы данных
class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename__ = "user"
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
