
from sqlalchemy.sql import func
from main import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    place_work = db.Column(db.String(50), nullable=False)

    time_id = db.Column(db.Integer, db.ForeignKey('times.id'))
    time = db.relationship('Time')

    

class Time(db.Model):
    __tablename__ = 'times'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, server_default=func.now())

    