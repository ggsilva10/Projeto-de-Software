import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///app.db')

db_session = scoped_session(sessionmaker (autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Habit(Base):
   __tablename__ = 'habit'
   id = Column(Integer, primary_key=True)
   nome = Column(String(100), nullable=False)
   descricao = Column(String(200))
   data_criacao = Column(Date, default=datetime.date.today)

   logs = relationship("HabitLog", back_populates="habit")


class HabitLog(Base): 
   __tablename__ = "habit_log"
   id = Column(Integer, primary_key=True)
   habit_id = Column(Integer, ForeignKey("habit.id"))
   data_criacao = Column(Date, default=datetime.date.today)
   status = Column(Boolean)

   habit = relationship("Habit", back_populates="logs")