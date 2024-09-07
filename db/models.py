from sqlalchemy import (Column, String,
                        Integer, ForeignKey, BigInteger,
                        DateTime, Float)
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base


# Модель Пользователя
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    surname = Column(String(55), nullable=False)
    name = Column(String(55), nullable=False)
    user_photo = Column(String)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_city = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


# Модель Карты
class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    card_number = Column(BigInteger, nullable=False)
    exp_date = Column(Integer, nullable=False)
    card_balance = Column(Float, nullable=False)
    cvv = Column(Integer, nullable=False)
    card_name = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery")


# Модель Транзакций
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, autoincrement=True, primary_key=True)
    card_from = Column(BigInteger, ForeignKey("cards.card_number"), name='card_from')
    amount = Column(Float, nullable=False)
    card_to = Column(BigInteger, ForeignKey("cards.card_number"), name='card_to')
    transfer_date = Column(DateTime, default=datetime.now())

    card_from_fk = relationship(Card, lazy="subquery", foreign_keys=[card_from])
    card_to_fk = relationship(Card, lazy="subquery", foreign_keys=[card_to])


class CorporativeClients(Base):
    __tablename__="corporative_clients"

    id = Column(Integer, autoincrement=True, primary_key=True)
    company= Column(String,nullable=False)
    type_of_bussiness=Column(String,nullable=False)


class Countries(Base):
    __tablename__ = "countrise"

    country_id = Column(Integer, autoincrement=True, primary_key=True)
    which_country=Column(String,nullable=False)
    countries_with_bonus=Column(String, nullable=False,default="Uzbekistan,Zimbabve")