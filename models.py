from sqlalchemy import Column, Integer, String, Date, Boolean
from database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    deadline = Column(Date)
    priority = Column(Integer)
    duration = Column(Integer)
    completed = Column(Boolean, default=False)