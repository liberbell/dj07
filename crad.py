from dataclasses import dataclass
from urllib.request import DataHandler
from app.assets.database import db_session
from app.assets.database import init_db
from app.assets.models import Data

import datetime

# init_db()
date = datetime.date.today()
print(date)
row = Data(date=DataHandler, subscribers=3500, reviews=200)