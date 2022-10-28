from database import db_session
from models import Data
from pandas as pd

data = db_session.query(Data.date, Data.subscribers, Data.reviews)