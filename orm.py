from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__) # объект приложения Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alinina.db' # привязываем базу данных
db = SQLAlchemy(app) # создаем объект SQLAlchemy

from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(8), unique=True, nullable=False)
    login = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    '''
    id_courses = db.Column(db.Integer, db.ForeignKey('courses.id'),
        nullable=False)
    lesson_amount = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    '''
    bthd = db.Column(db.DateTime, nullable=False)
    '''
    course = db.relationship('Courses',
        backref=db.backref('users', lazy=False))
    '''
    def __repr__(self):
        return f'{self.id} {self.name}'

db.create_all()
