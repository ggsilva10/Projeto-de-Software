import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), default='#007bff')
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    habits = db.relationship('Habit', backref="category", lazy=True)

class Habit(db.Model):
   __tablename__ = 'habits'
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   description = db.Column(db.String(200))
   creation_date = db.Column(db.Date, default=datetime.date.today)
   owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
   category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
   logs = db.relationship('HabitLog', back_populates='habit', lazy=True, cascade="all, delete-orphan")


class HabitLog(db.Model): 
   __tablename__ = "habit_logs"
   id = db.Column(db.Integer, primary_key=True)
   habit_id = db.Column(db.Integer, db.ForeignKey("habits.id"), nullable=False)
   creation_date = db.Column(db.Date, default=datetime.date.today)
   is_completed = db.Column(db.Boolean, default=False)
   habit = db.relationship("Habit", back_populates="logs")

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    habits = db.relationship('Habit', backref='owner', lazy=True, cascade="all, delete-orphan")

    categories = db.relationship('Category', backref='owner', lazy=True, cascade="all, delete-orphan")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = generate_password_hash(plain_text_password)

    def check_password(self, attempted_password):
        return check_password_hash(self.password_hash, attempted_password)