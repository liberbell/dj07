from database import db_session
from models import Data
import pandas as pd

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()
print(data)
print(data[0].subscribers)
print(data[0].date)

dates = []
subscribers = []
reviews = []

for datum in data:
    dates.append(datum.data)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)