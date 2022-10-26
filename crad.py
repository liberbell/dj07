from dataclasses import dataclass
from urllib.request import DataHandler
from app.assets.database import db_session
from app.assets.database import init_db
from app.assets.models import Data

import datetime

# init_db()
date = datetime.date.today()
# print(date)
row = Data(date=date, subscribers=3500, reviews=200)
# print(row.date, row.subscribers, row.reviews)
# db_session.add(row)
# db_session.commit()

row1 = Data(date=date, subscribers=6500, reviews=210)
row2 = Data(date=date, subscribers=1500, reviews=220)
# db_session.add(row1)
# db_session.add(row2)
# db_session.commit()

# print(db_session.query(Data).all()[0].subscribers)

datam = db_session.query(Data)[0]
datam.subscribers = 10000
db_session.add(datam)
db_session.commit()