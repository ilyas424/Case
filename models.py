
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

    

class Time(db.Model):
    __tablename__ = 'times'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref("times", lazy=True))