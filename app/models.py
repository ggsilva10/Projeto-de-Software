import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Habit(db.Model):
   __tablename__ = 'habit'
   id = db.Column(db.Integer, primary_key=True)
   nome = db.Column(db.String(100), nullable=False)
   descricao = db.Column(db.String(200))
   data_criacao = db.Column(db.Date, default=datetime.date.today)

   owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

   logs = db.relationship('HabitLog', back_populates='habit', lazy=True, cascade="all, delete-orphan")


class HabitLog(db.Model): 
   __tablename__ = "habit_log"
   id = db.Column(db.Integer, primary_key=True)
   habit_id = db.Column(db.Integer, db.ForeignKey("habit.id"), nullable=False)
   data_criacao = db.Column(db.Date, default=datetime.date.today)
   status = db.Column(db.Boolean, default=False)
   habit = db.relationship("Habit", back_populates="logs")

class User(db.Model, UserMixin):
   __tablename__="user"
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False)
   password_hash = db.Column(db.String(128), nullable=False)

   habits = db.relationship('Habit', backref="owner", lazy=True, cascade="all, delete-orphan")

@property
def password(self):
   raise AttributeError("password is not a readable attribute")

@password.setter
def password(self, plain_text_password):
   self.password_hash = generate_password_hash(plain_text_password)

def check_password(self, attempted_password):
   return check_password_hash(self.password_hash, attempted_password)