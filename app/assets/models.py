from enum import unique
import imp
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from assets.database import Base
from datetime import datetime as dt

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=False)
    subscribers = Column(Integer, unique=False)