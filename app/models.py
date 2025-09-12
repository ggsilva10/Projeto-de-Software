import datetime
from . import db

class Habit(db.Model):
   __tablename__ = 'habit'
   id = db.Column(db.Integer, primary_key=True)
   nome = db.Column(db.String(100), nullable=False)
   descricao = db.Column(db.String(200))
   data_criacao = db.Column(db.Date, default=datetime.date.today)
   logs = db.relationship('HabitLog', back_populates='habit', lazy=True, cascade="all, delete-orphan")


class HabitLog(db.Model): 
   __tablename__ = "habit_log"
   id = db.Column(db.Integer, primary_key=True)
   habit_id = db.Column(db.Integer, db.ForeignKey("habit.id"), nullable=False)
   data_criacao = db.Column(db.Date, default=datetime.date.today)
   status = db.Column(db.Boolean, default=False)
   habit = db.relationship("Habit", back_populates="logs")