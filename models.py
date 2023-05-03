from datetime import datetime
from main import db


class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)


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
    creation_date = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%b-%d %H:%M:%S"))


class Statistic(db.Model):
    __tablename__ = 'Staistic'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    action = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())

